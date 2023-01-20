from __future__ import annotations

import traceback
from io import StringIO
from typing import TYPE_CHECKING, List

from js_pyi.conversion import to_py_type, to_py_value, to_py_name

if TYPE_CHECKING:
    from js_pyi.datamodel import *


def s_attribute(a: GAttribute) -> str:
    return to_py_name(a.name) + ': ' + s_annotation(a.annotation)


def s_arg(a: GArg) -> str:
    default = ''
    if a.default is not None:
        default = ' = ' + to_py_value(a.default)
    return to_py_name(a.name) + ': ' + s_annotation(a.annotation) + default


def s_interface(i: GInterface) -> str:
    bases = ''
    if len(i.bases) > 0:
        bases = '(' + ', '.join(i.bases) + ')'
    decl = f'class {i.name}{bases}:'
    if len(i.body) == 0:
        return decl + ' ...'
    for b in i.body:
        decl += '\n' + (' ' * 4) + b.to_python()
    return decl


def s_method(m: GMethod) -> str:
    returns = ''
    if m.returns is not None and m.returns != 'undefined':
        returns = ' -> ' + s_annotation(m.returns)

    args_arr = ['self'] + [s_arg(a) for a in m.arguments]
    args_str = ', '.join(args_arr)
    name = m.name
    return f'def {name}({args_str}){returns}: ...'


def s_annotation(a: GAnnotation) -> str:
    if isinstance(a, str):
        return s_annotation([a])
    if isinstance(a, list):
        return ' | '.join([to_py_type(e) for e in a])

    unhandled(a)


def s_unhandled(u: GUnhandled) -> str:
    ex_str = ''
    if u.exception is not None:
        ex_str = ''.join(traceback.TracebackException.from_exception(u.exception).format())
        ex_str += '\n' + ('-' * 50) + '\n'
    return ex_str + u.body


def s_statements(statements: List[GStmt]) -> str:
    res = StringIO()
    for st in statements:
        res.write(st.to_python() + '\n')
    getvalue = res.getvalue()
    return getvalue
