from __future__ import annotations

from itertools import groupby
from typing import List

from js_pyi.datamodel import GStmt, GUnhandled, GClass, GInclude, expect_isinstance
from js_pyi.itertools import partition, groupby


def merge(statements: List[GStmt]) -> List[GStmt]:
    unhandled, handled = partition(statements, lambda e: isinstance(e, GUnhandled))
    result: List[GStmt] = []
    by_name = groupby(handled, lambda stmt: stmt.name)
    # { 'Doc' : [ GClass('Doc', ... ), GClass('Doc', ...), GInclude('Doc', ...) ] , ... }
    for name, sts_for_name in by_name.items():
        if GClass in map(lambda s: type(s), sts_for_name):
            mi = _m_class(name, sts_for_name)
            result.append(mi)
        else:
            raise Exception(f"Don't know how to merge name `{name}`\n{sts_for_name}")

    return result + unhandled


def _m_class(name, sts_for_name):
    by_type = groupby(sts_for_name, lambda s: type(s))
    # { GClass : [ ... ] , GInclude : [ ... ] }
    class_stmts = by_type.pop(GClass)
    class_stmt = _m_gclasses(class_stmts)
    include_stmts = by_type.pop(GInclude, None)
    if include_stmts is not None:
        _m_class_include(class_stmt, include_stmts)
    return class_stmt


def _m_gclasses(statements: List[GClass]) -> GClass:
    # check pre-conditions
    name = None
    for st in statements:
        expect_isinstance(st, GClass)
        if name is None:
            name = st.name
        else:
            assert st.name == name

    result = GClass(name)
    for st in statements:
        result.bases.extend(st.bases)
        result.body.extend(st.body)
    return result


def _m_class_include(class_stmt: GClass, include_stmts: List[GInclude]):
    for inc in include_stmts:
        class_stmt.bases.append(inc.includes)
