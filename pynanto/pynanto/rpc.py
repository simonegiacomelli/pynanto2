from inspect import getmembers, isfunction, signature, iscoroutinefunction
from types import ModuleType
from typing import NamedTuple, List


class Function(NamedTuple):
    name: str
    signature: str
    is_coroutine_function: bool


class Rpc:
    def add(self, module: ModuleType):
        pass


class Module:
    def __init__(self, module: ModuleType):
        self.module = module
        self.name = module.__name__

        def std_fun2Function(fun_tuple) -> Function:
            name = fun_tuple[0]
            func = fun_tuple[1]
            sign = signature(func)
            return Function(name, str(sign), iscoroutinefunction(func))

        self.functions: List[Function] = list(map(std_fun2Function, getmembers(self.module, isfunction)))
