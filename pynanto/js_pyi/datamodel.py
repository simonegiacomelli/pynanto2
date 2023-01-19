from __future__ import annotations

import typing
from dataclasses import dataclass, field
from typing import List, Optional

from js_pyi.stringify import g_method, g_attribute


@dataclass()
class GStmt:
    pass


@dataclass()
class GUnhandled(GStmt):
    body: str
    exception: Exception | None


@dataclass()
class GInterface:
    name: str
    bases: List[str] = field(default_factory=list)
    body: List[GStmt] = field(default_factory=list)


GAnnotation = typing.Union[str, List[str]]


@dataclass()
class GNamedAnnotation(GStmt):
    name: str
    annotation: GAnnotation


@dataclass()
class GAttribute(GNamedAnnotation):
    def as_python(self): return g_attribute(self)


@dataclass
class GArg(GNamedAnnotation):
    default: Optional[str] = None


@dataclass
class GMethod(GStmt):
    name: str
    arguments: List[GArg] = field(default_factory=list)
    returns: Optional[GAnnotation] = 'undefined'

    def as_python(self): return g_method(self)


def unhandled(argument):
    raise Exception(f'todo unhandled type={type(argument)} `{argument}`')


def expect_type(instance, expected_type):
    if not isinstance(instance, expected_type):
        raise Exception(f' expect instance to be `{expected_type}` '
                        f'but instead found to be `{type(instance)}`')
