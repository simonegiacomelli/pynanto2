from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from js_pyi.g_dataclasses import *


def g_attribute(a: GAttribute) -> str:
    return g_named_annotation(a)


def g_annotation(a: GAnnotation) -> str:
    return _to_py_type(a)


def g_named_annotation(na: GNamedAnnotation) -> str:
    return na.name + ': ' + g_annotation(na.annotation)


def g_arg(a: GArg) -> str:
    default = ''
    if a.default is not None:
        default = ' = ' + a.default
    return g_named_annotation(a) + default


def g_method(m: GMethod) -> str:
    returns = ''
    if m.returns is not None and m.returns != 'undefined':
        returns = ' -> ' + g_annotation(m.returns)

    args_arr = [g_arg(a) for a in m.arguments]
    args_str = ', '.join(args_arr)
    return f'def {m.name}({args_str}){returns}: ...'


_types_dict = {
    'DOMString': 'str'
}


def _to_py_type(s: str) -> str:
    return _types_dict.get(s, s)
