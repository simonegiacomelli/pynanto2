from __future__ import annotations

from js_pyi.ingest import ingest
from js_pyi.is_test import _append_base
from js_pyi.merge import merge


def test_merge():
    piece1 = ingest('interface Doc : Blob  { attribute Blob foo; }')
    piece2 = ingest('partial interface Doc  { attribute Element bar; }')

    expected = ingest('interface Doc : Blob {  attribute Blob foo; attribute Element bar; }')

    actual = merge(piece1 + piece2)
    assert actual == expected


def test_merge_include():
    piece1 = ingest('interface Doc : Blob  { attribute Blob foo; }')
    piece2 = ingest('partial interface Doc  { attribute Element bar; }')
    piece3 = ingest('Doc includes Bar; Doc includes Baz')

    actual = merge(piece1 + piece2 + piece3)

    expected = ingest('interface Doc : Blob {  attribute Blob foo; attribute Element bar; }')
    _append_base(expected[0], 'Bar')
    _append_base(expected[0], 'Baz')

    assert actual == expected


# def test_merge_method_overload():
#     idl = 'Blob foo();\n Blob foo(bool arg);'
#     actual = merge(ingest(idl))
#     expected = ingest('undefined alert')
#     assert actual ==

def test_merge_partition_by_name():
    pass
