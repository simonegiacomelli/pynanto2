import typing
from dataclasses import dataclass, field
from typing import List, Any, Optional

from js_pyi.generate import g_method, g_attribute


@dataclass()
class GAst:
    pass


@dataclass()
class GExpr(GAst):
    pass


@dataclass()
class GStmt(GAst):
    pass


@dataclass()
class GUnhandled(GStmt):
    body: str
    exception: Exception


@dataclass()
class GInterface:
    name: str
    bases: List[str] = field(default_factory=list)
    body: List[GStmt] = field(default_factory=list)


class GUnion(List[str]):
    pass


GType = typing.Union[str, GUnion]


@dataclass()
class GOptional:
    of: GType


GAnnotation = typing.Union[GType, GOptional]


@dataclass()
class GAttribute(GStmt):
    name: str
    annotation: GAnnotation

    def __repr__(self): return g_attribute(self)


@dataclass
class GArg:
    name: str
    annotation: GAnnotation
    default: Optional[str] = None


@dataclass
class GArguments:
    posonlyargs: List[Any] = ()
    args: List[GArg] = ()
    vararg: List[Any] = ()
    kwonlyargs: List[Any] = ()
    kw_defaults: List[Any] = ()
    kwarg: List[Any] = ()
    defaults: List[Any] = ()


@dataclass
class GMethod(GStmt):
    name: str
    arguments: GArguments
    returns: str

    def __repr__(self): return g_method(self)
