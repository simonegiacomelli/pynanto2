from __future__ import annotations

import typing
from dataclasses import dataclass, field
from typing import List, Optional

from js_pyi.stringify import s_method, s_attribute, s_interface, s_unhandled, s_enum, s_arg


@dataclass()
class GStmt:
    def to_python(self) -> str:
        raise Exception(f'not implemented {type(self)}')


@dataclass()
class GRootStmt(GStmt):
    name: str
    body: List[GStmt] = field(default_factory=list)


@dataclass()
class GUnhandled(GStmt):
    body_str: str
    exception: Exception | None = None

    def to_python(self): return s_unhandled(self)


@dataclass()
class GUnhandledRoot(GUnhandled):
    pass


@dataclass()
class GUnhandledNested(GUnhandled):
    pass


@dataclass()
class GGeneric:
    type: str
    gen_type: str


@dataclass()
class GInterface(GRootStmt):
    bases: List[str] = field(default_factory=list)

    def to_python(self): return s_interface(self)


GType = typing.Union[str, GGeneric]
GAnnotation = typing.Union[GType, List[GType]]


@dataclass()
class GNamedAnnotation(GStmt):
    name: str
    annotation: GAnnotation


@dataclass()
class GAttribute(GNamedAnnotation):
    def to_python(self): return s_attribute(self)


@dataclass
class GArg(GNamedAnnotation):
    default: Optional[str] = None

    def to_python(self): return s_arg(self)
@dataclass
class GMethod(GStmt):
    name: str
    arguments: List[GArg] = field(default_factory=list)
    returns: Optional[GAnnotation] = 'undefined'

    def to_python(self): return s_method(self)


@dataclass
class GEnum(GRootStmt):
    def to_python(self): return s_enum(self)


@dataclass()
class GEnumValue(GStmt):
    value: str


def unhandled(argument):
    raise Exception(f'unhandled type={type(argument)} `{argument}`')


def expect_type(instance, expected_type):
    if not isinstance(instance, expected_type):
        raise Exception(f' expect instance to be `{expected_type}` '
                        f'but instead found to be `{type(instance)}`')
