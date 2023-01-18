import typing
from dataclasses import dataclass, field
from typing import List, Optional

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


@dataclass()
class GOptional:
    of: 'GAnnotation'


GAnnotation = typing.Union[str, GUnion, GOptional]


@dataclass()
class GNamedAnnotation(GStmt):
    name: str
    annotation: GAnnotation


@dataclass()
class GAttribute(GNamedAnnotation):
    def __repr__(self): return g_attribute(self)


@dataclass
class GArg(GNamedAnnotation):
    default: Optional[str] = None


@dataclass
class GArguments:
    args: List[GArg] = ()


@dataclass
class GMethod(GStmt):
    name: str
    arguments: GArguments
    returns: str

    def __repr__(self): return g_method(self)
