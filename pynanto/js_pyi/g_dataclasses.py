from __future__ import annotations

import typing
from dataclasses import dataclass, field
from typing import List, Optional

from js_pyi.generate import g_method, g_attribute


@dataclass()
class GStmt:
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


@dataclass()
class GNullable:
    of: 'GAnnotation'


GUnion = typing.NewType('GUnion', list)

GAnnotation = typing.Union[str, GUnion, GNullable]


class GUnion(List[GAnnotation]):
    pass


@dataclass()
class GNamedAnnotation(GStmt):
    name: str
    annotation: GAnnotation


@dataclass()
class GAttribute(GNamedAnnotation):
    def str(self): return g_attribute(self)


@dataclass
class GArg(GNamedAnnotation):
    default: Optional[str] = None
    optional: bool = False
    """`optional` in webidl lingo and not in python sense"""


@dataclass
class GMethod(GStmt):
    name: str
    arguments: List[GArg] = field(default_factory=list)
    returns: Optional[GAnnotation] = None

    def str(self): return g_method(self)
