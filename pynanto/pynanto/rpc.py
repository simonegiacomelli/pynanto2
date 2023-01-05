import importlib
from inspect import getmembers, isfunction, signature, iscoroutinefunction
from types import ModuleType, FunctionType
from typing import NamedTuple, List, Union


class Function(NamedTuple):
    name: str
    func: FunctionType
    signature: str
    is_coroutine_function: bool


class Introspection:
    def __init__(self, module: Union[str, ModuleType]):
        if isinstance(module, str):
            module = importlib.import_module(module)
        self.module = module
        self.name = module.__name__

        def std_fun2function(fun_tuple) -> Function:
            name = fun_tuple[0]
            func = fun_tuple[1]
            sign = signature(func)
            return Function(name, func, str(sign), iscoroutinefunction(func))

        self.functions: List[Function] = list(map(std_fun2function, getmembers(self.module, isfunction)))

    def invoke(self, name: str, *args):
        for f in self.functions:
            if f.name == name:
                return f.func(*args)
