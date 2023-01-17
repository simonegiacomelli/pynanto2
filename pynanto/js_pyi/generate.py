from dataclasses import dataclass
from typing import List, Any


@dataclass()
class GAst:
    ...


@dataclass()
class GExpr(GAst):
    ...


@dataclass()
class GStmt(GAst):
    ...


@dataclass()
class GWithName:
    name: str


@dataclass()
class GName:
    name: str


@dataclass()
class GClassDef:
    name: str
    bases: List[str] = ()
    body: List[GStmt] = ()


@dataclass
class GArguments:
    posonlyargs: List[Any] = ()
    args: List[Any] = ()
    vararg: List[Any] = ()
    kwonlyargs: List[Any] = ()
    kw_defaults: List[Any] = ()
    kwarg: List[Any] = ()
    defaults: List[Any] = ()


@dataclass
class GArg:
    name: str
    annotation: str


@dataclass
class GFunctionDef(GStmt):
    name: str
    arguments: GArguments
    returns: str


class GModule(List[GStmt]):
    pass
