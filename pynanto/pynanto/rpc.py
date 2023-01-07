import json
from inspect import getmembers, isfunction, signature, iscoroutinefunction, Signature
from types import ModuleType, FunctionType
from typing import NamedTuple, List, Tuple, Any, Optional, Dict, Callable, Awaitable

from typing_extensions import Protocol

from pynanto.response import Request, Response
from pynanto.routes import Route
from pynanto.unsync import unsync


class Function(NamedTuple):
    name: str
    func: FunctionType
    signature: str
    is_coroutine_function: bool
    sign: Signature
    blocking: FunctionType


def _std_function_to_function(fun_tuple: Tuple[str, FunctionType]) -> Function:
    name = fun_tuple[0]
    func = fun_tuple[1]
    sign = signature(func)
    is_coroutine_function = iscoroutinefunction(func)
    blocking = unsync(func)
    return Function(name, func, str(sign), is_coroutine_function, signature(func), blocking)


class Module:
    def __init__(self, module: ModuleType):
        self.module = module
        self.name = module.__name__

        self.functions: List[Function] = function_list(self.module)
        self._funcs = {f.name: f for f in self.functions}

    def __getitem__(self, name) -> Function:
        return self._funcs.get(name, None)


def function_list(module: ModuleType) -> List[Function]:
    return list(map(_std_function_to_function, getmembers(module, isfunction)))


class RpcResponse:
    @classmethod
    def from_json(cls, string: str) -> Any:
        return json.loads(string)

    @classmethod
    def to_json(cls, response: Any) -> str:
        return json.dumps(response)


class RpcRequest(NamedTuple):
    module: str
    func: str
    args: List[Optional[Any]]

    def json(self) -> str:
        return json.dumps(self)

    @classmethod
    def build_request(cls, module_name: str, func_name: str, *args) -> 'RpcRequest':
        return RpcRequest(module_name, func_name, args)

    @classmethod
    def from_json(cls, string: str) -> 'RpcRequest':
        obj = json.loads(string)
        request = RpcRequest(*obj)
        return request


Fetch = Callable[[str, str, str], Awaitable[str]]


class Fetch(Protocol):
    def __call__(self, url: str, method: str = '', data: str = '') -> Awaitable[str]: ...


class Proxy:
    def __init__(self, module_name: str, rpc_url: str, fetch: Fetch):
        self.rpc_url = rpc_url
        self.fetch = fetch
        self.module_name = module_name

    async def dispatch(self, func_name: str, *args) -> Any:
        rpc_request = RpcRequest.build_request(self.module_name, func_name, *args)
        json_response = await self.fetch(self.rpc_url, method='POST', data=rpc_request.json())
        return RpcResponse.from_json(json_response)


class Services:
    def __init__(self):
        self._modules: Dict[str, Module] = {}
        self.route = Route('/pynanto/rpc', self._route_callback)

    def add_module(self, module: Module):
        self._modules[module.name] = module

    def find_module(self, module_name: str) -> Optional[Module]:
        return self._modules.get(module_name, None)

    def dispatch(self, request: str) -> str:
        rpc_request = RpcRequest.from_json(request)
        module = self.find_module(rpc_request.module)
        function = module[rpc_request.func]
        result = function.blocking(*rpc_request.args)
        return RpcResponse.to_json(result)

    def _route_callback(self, request: Request) -> Response:
        resp = self.dispatch(request.content)
        response = Response(resp, 'application/json')
        return response


def generate_stub_source(module: Module, rpc_url: str, imports: str):
    module_name = module.name
    # language=python
    stub_header = f"""
from pynanto.rpc import Proxy
{imports}

rpc_url = '{rpc_url}'
module_name = '{module_name}'
proxy = Proxy(module_name, rpc_url, async_fetch_str)
    """

    stub_functions = ''
    for f in module.functions:
        parameters = f.sign.parameters.values()
        args_list = ''.join(map(lambda p: ', ' + p, (p.name for p in parameters)))
        fun_stub = f'\nasync def {f.name}{f.signature}:\n' + \
                   f'    return await proxy.dispatch("{f.name}"{args_list})\n'
        stub_functions += fun_stub

    return stub_header + stub_functions
