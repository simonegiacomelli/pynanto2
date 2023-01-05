from inspect import getmembers, isfunction, signature, iscoroutinefunction
from types import ModuleType, FunctionType
from typing import NamedTuple, List, Tuple


class Function(NamedTuple):
    name: str
    func: FunctionType
    signature: str
    is_coroutine_function: bool


class Introspection:
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
