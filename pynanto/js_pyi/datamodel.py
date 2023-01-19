from __future__ import annotations

import typing
from dataclasses import dataclass, field
from typing import List, Optional

from js_pyi.stringify import g_method, g_attribute, g_interface


@dataclass()
class GStmt:
    def to_python(self) -> str:
        raise Exception(f'not implemented {type(self)}')


@dataclass()
class GUnhandled(GStmt):
    body: str
    exception: Exception | None = None


@dataclass()
class GGeneric:
    type: str
    gen_type: str


@dataclass()
class GInterface(GStmt):
    name: str
    bases: List[str] = field(default_factory=list)
    body: List[GStmt] = field(default_factory=list)

    def to_python(self): return g_interface(self)


GType = typing.Union[str, GGeneric]
GAnnotation = typing.Union[GType, List[GType]]


@dataclass()
class GNamedAnnotation(GStmt):
    name: str
    annotation: GAnnotation


@dataclass()
class GAttribute(GNamedAnnotation):
    def to_python(self): return g_attribute(self)


@dataclass
class GArg(GNamedAnnotation):
    default: Optional[str] = None


@dataclass
class GMethod(GStmt):
    name: str
    arguments: List[GArg] = field(default_factory=list)
    returns: Optional[GAnnotation] = 'undefined'

    def to_python(self): return g_method(self)


def unhandled(argument):
    raise Exception(f'unhandled type={type(argument)} `{argument}`')


def expect_type(instance, expected_type):
    if not isinstance(instance, expected_type):
        raise Exception(f' expect instance to be `{expected_type}` '
                        f'but instead found to be `{type(instance)}`')
