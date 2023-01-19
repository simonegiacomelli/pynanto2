from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from js_pyi.datamodel import *


def g_attribute(a: GAttribute) -> str:
    return g_named_annotation(a)


def g_named_annotation(na: GNamedAnnotation) -> str:
    return na.name + ': ' + g_annotation(na.annotation)


def g_arg(a: GArg) -> str:
    default = ''
    if a.default is not None:
        default = ' = ' + _to_py_value(a.default)
    return g_named_annotation(a) + default


def g_method(m: GMethod) -> str:
    returns = ''
    if m.returns is not None and m.returns != 'undefined':
        returns = ' -> ' + g_annotation(m.returns)

    args_arr = ['self'] + [g_arg(a) for a in m.arguments]
    args_str = ', '.join(args_arr)
    return f'def {m.name}({args_str}){returns}: ...'


def g_annotation(a: GAnnotation) -> str:
    if isinstance(a, str):
        return g_annotation([a])
    if isinstance(a, list):
        return ' | '.join([_to_py_type(e) for e in a])

    from js_pyi.datamodel import GNullable
    if isinstance(a, GNullable):
        return g_annotation(a.of) + ' | None'

    unhandled(a)


_types_dict = {
    'DOMString': 'str',
    'long': 'int'
}


def _to_py_type(s) -> str:
    return _types_dict.get(s, s)


_values_dict = {
    'null': 'None',
}


def _to_py_value(s) -> str:
    return _values_dict.get(s, s)