import json
from inspect import getmembers, isfunction, signature, iscoroutinefunction
from types import ModuleType, FunctionType
from typing import NamedTuple, List, Tuple, Any, Optional, Dict


class Function(NamedTuple):
    name: str
    func: FunctionType
    signature: str
    is_coroutine_function: bool


class Module:
    def __init__(self, module: ModuleType):
        self.module = module
        self.name = module.__name__

        self.functions: List[Function] = function_list(self.module)
        self._funcs = {f.name: f for f in self.functions}

    def __getitem__(self, name) -> Function:
        return self._funcs.get(name, None)


def _std_function_to_function(fun_tuple: Tuple[str, FunctionType]) -> Function:
    name = fun_tuple[0]
    func = fun_tuple[1]
    sign = signature(func)
    return Function(name, func, str(sign), iscoroutinefunction(func))


def function_list(module) -> List[Function]:
    return list(map(_std_function_to_function, getmembers(module, isfunction)))


class RpcRequest(NamedTuple):
    callable_path: str
    args: List[Optional[Any]]

    def json(self) -> str:
        return json.dumps(self)

    @classmethod
    def build_request(cls, callable_path: str, *args) -> 'RpcRequest':
        return RpcRequest(callable_path, args)

    @classmethod
    def from_json(cls, string: str) -> 'RpcRequest':
        obj = json.loads(string)
        request = RpcRequest(*obj)
        return request


class Services:
    def __init__(self):
        self._modules: Dict[str, Module] = {}

    def add_module(self, module: Module):
        self._modules[module.name] = module

    def find_module(self, module_name: str) -> Optional[Module]:
        return self._modules.get(module_name, None)
