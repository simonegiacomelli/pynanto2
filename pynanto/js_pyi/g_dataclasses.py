from __future__ import annotations

from dataclasses import dataclass, field
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
    bases: List[str] = field(default_factory=list)
    body: List[GStmt] = field(default_factory=list)


@dataclass
class GArguments:
    posonlyargs: List[Any] = ()
    args: List[Any] = ()
    vararg: List[Any] = ()
    kwonlyargs: List[Any] = ()
    kw_defaults: List[Any] = ()
    kwarg: List[Any] = ()
    defaults: List[Any] = ()


@dataclass()
class GUnion:
    annotations: List[str]


@dataclass
class GArg:
    name: str
    annotation: str | GUnion


@dataclass
class GFunctionDef(GStmt):
    name: str
    arguments: GArguments
    returns: str


class GModule(List[GStmt]):
    pass
