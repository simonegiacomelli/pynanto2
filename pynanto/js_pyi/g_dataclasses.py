from __future__ import annotations

import typing
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


@dataclass()
class GUnion:
    annotations: List[str]


GAnnotation = typing.Union[str, GUnion]


@dataclass()
class GAttribute(GStmt):
    name: str
    annotation: GAnnotation


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
    annotation: GAnnotation
    default: str | None = None


@dataclass
class GFunctionDef(GStmt):
    name: str
    arguments: GArguments
    returns: str


class GModule(List[GStmt]):
    pass
