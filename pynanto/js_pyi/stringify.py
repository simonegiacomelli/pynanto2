from __future__ import annotations

from typing import TYPE_CHECKING

from js_pyi.conversion import to_py_type, to_py_value, to_py_name

if TYPE_CHECKING:
    from js_pyi.datamodel import *


def g_attribute(a: GAttribute) -> str:
    return to_py_name(a.name) + ': ' + g_annotation(a.annotation)


def g_arg(a: GArg) -> str:
    default = ''
    if a.default is not None:
        default = ' = ' + to_py_value(a.default)
    return to_py_name(a.name) + ': ' + g_annotation(a.annotation) + default


def g_interface(i: GInterface) -> str:
    bases = ''
    if len(i.bases) > 0:
        bases = '(' + ', '.join(i.bases) + ')'
    decl = f'class {i.name}{bases}:'
    if len(i.body) == 0:
        return decl + ' ...'
    for b in i.body:
        decl += '\n' + (' ' * 4) + b.to_python()
    return decl


def g_method(m: GMethod) -> str:
    returns = ''
    if m.returns is not None and m.returns != 'undefined':
        returns = ' -> ' + g_annotation(m.returns)

    args_arr = ['self'] + [g_arg(a) for a in m.arguments]
    args_str = ', '.join(args_arr)
    name = m.name
    return f'def {name}({args_str}){returns}: ...'


def g_annotation(a: GAnnotation) -> str:
    if isinstance(a, str):
        return g_annotation([a])
    if isinstance(a, list):
        return ' | '.join([to_py_type(e) for e in a])

    from js_pyi.datamodel import GOptional
    if isinstance(a, GOptional):
        return g_annotation(a.of) + ' | None'

    unhandled(a)
