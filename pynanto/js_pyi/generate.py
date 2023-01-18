from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from js_pyi.g_dataclasses import *


def g_attribute(a: GAttribute) -> str:
    return a.name + ': ' + a.annotation


_types_dict = {
    'DOMString': 'str'
}


def _to_py_type(s: str) -> str:
    return _types_dict.get(s, s)


def g_method(m: GMethod) -> str:
    returns = ''
    if m.returns != 'undefined':
        returns = ' -> ' + _to_py_type(m.returns)

    return f'def {m.name}(){returns}: ...'
