from __future__ import annotations

import typing
from dataclasses import dataclass, field
from typing import List, Optional

from js_pyi.stringify import s_method, s_attribute, s_interface, s_unhandled, s_enum, s_arg, s_typedef


class GPythonProducer:

    def to_python(self) -> str:
        raise Exception(f'not implemented {type(self)}')


@dataclass()
class GStmt:
    pass


@dataclass()
class GIgnoredStmt(GStmt):
    body_str: str


@dataclass()
class GRootStmt(GStmt):
    pass


@dataclass()
class GNameAndBody(GStmt):
    name: str
    body: List[GStmt] = field(default_factory=list)


@dataclass()
class GUnhandled(GStmt):
    body_str: str
    exception: Exception | None = None

    def to_python(self): return s_unhandled(self)


@dataclass()
class GUnhandledRoot(GUnhandled, GRootStmt):
    pass


@dataclass()
class GUnhandledNested(GUnhandled):
    pass


@dataclass()
class GGeneric:
    type: str
    gen_type: str


@dataclass()
class GClass(GNameAndBody, GRootStmt, GPythonProducer):
    bases: List[str] = field(default_factory=list)

    def to_python(self): return s_interface(self)


GType = typing.Union[str, GGeneric]
GAnnotation = typing.Union[GType, List[GType]]


@dataclass()
class GNamedAnnotation(GStmt):
    name: str
    annotation: GAnnotation = field(default_factory=list)


@dataclass()
class GAttribute(GNamedAnnotation, GPythonProducer):
    def to_python(self): return s_attribute(self)


@dataclass()
class GGeneric(GNamedAnnotation):
    pass


@dataclass
class GArg(GNamedAnnotation, GPythonProducer):
    default: Optional[str] = None

    def to_python(self): return s_arg(self)


@dataclass
class GMethod(GStmt, GPythonProducer):
    name: str
    arguments: List[GArg] = field(default_factory=list)
    returns: Optional[GAnnotation] = 'undefined'

    def to_python(self): return s_method(self)


@dataclass()
class GInclude(GRootStmt):
    name: str
    includes: str


@dataclass()
class GTypedef(GRootStmt, GPythonProducer):
    name: str
    annotation: GAnnotation = field(default_factory=list)

    def to_python(self): return s_typedef(self)


@dataclass
class GEnum(GNameAndBody, GRootStmt, GPythonProducer):
    def to_python(self): return s_enum(self)


@dataclass()
class GEnumValue(GStmt, GPythonProducer):
    value: str
