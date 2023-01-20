"""ingest and stringify tests"""
from __future__ import annotations

import widlparser

from js_pyi.datamodel import *
from js_pyi.ingest import ingest, i_construct, merge, discard_unhandled


def test_attribute():
    _verify_2nd_level_construct(
        'attribute Blob foo;',
        'foo: Blob',
        GAttribute('foo', 'Blob'),
    )


def test_method_no_params():
    _verify_2nd_level_construct(
        'undefined foo();',
        'def foo(self): ...',
        GMethod('foo'),
    )


def test_name_clash_async():
    _verify_2nd_level_construct(
        'undefined foo (Blob async);',
        'def foo(self, async_: Blob): ...',
        GMethod('foo', [GArg('async', 'Blob')])
    )


def test_nullable():
    _verify_2nd_level_construct(
        'undefined foo (DOMString? name);',
        'def foo(self, name: str | None): ...',
        GMethod('foo', [GArg('name', ['DOMString', 'None'])])
    )


def test_float():
    _verify_2nd_level_construct(
        'undefined foo (float x);',
        'def foo(self, x: float): ...',
        GMethod('foo', [GArg('x', 'float')])
    )


def test_unsupported__generics():
    idl = 'Blob foo ((Blob or sequence<Blob>) bar);'
    actual_model = _2nd_level_construct(idl, throw=False)
    assert GUnhandled == type(actual_model)


def test_unsupported__attribute_names():
    idl = 'attribute object global;'
    actual_model = _2nd_level_construct(idl, throw=False)
    assert GUnhandled == type(actual_model)

    idl = 'attribute object as;'
    actual_model = _2nd_level_construct(idl, throw=False)
    assert GUnhandled == type(actual_model)


def test_unsupported__comments():
    idl = 'Blob foo(optional Blob bar = 0  /* comment */ );'
    actual_model = _2nd_level_construct(idl, throw=False)
    assert GUnhandled == type(actual_model)


def test_nullable_result():
    _verify_2nd_level_construct(
        'Blob? foo();',
        'def foo(self) -> Blob | None: ...',
        GMethod('foo', returns=['Blob', 'None'])
    )


def test_compound_nullable():
    _verify_2nd_level_construct(
        'undefined foo( (HTMLElement or long)? before );',
        'def foo(self, before: HTMLElement | int | None): ...',
        GMethod('foo', [GArg('before', ['HTMLElement', 'long', 'None'])])
    )


def test_optional():
    _verify_2nd_level_construct(
        'undefined foo(optional Blob label);',
        'def foo(self, label: Blob | None = None): ...',
        GMethod('foo', [GArg('label', ['Blob', 'None'], 'None')])
    )


def test_optional_with_default():
    _verify_2nd_level_construct(
        'undefined foo(optional DOMString label = "foobar");',
        'def foo(self, label: str | None = "foobar"): ...',
        GMethod('foo', [GArg('label', ['DOMString', 'None'], '"foobar"')])
    )


def test_compound_nullable_optional_default():
    _verify_2nd_level_construct(
        'undefined foo( optional (HTMLElement or long)? before = null);',
        'def foo(self, before: HTMLElement | int | None = None): ...',
        GMethod('foo', [
            GArg('before', ['HTMLElement', 'long', 'None'], 'null')
        ]),
    )


def test_interface():
    actual = ingest("""
interface Document : Blob {
FooElement createElement(DOMString localName);
}    
""")

    assert actual == [GInterface(
        'Document', bases=['Blob'], body=[
            (GMethod('createElement', arguments=[GArg('localName', 'DOMString')],
                     returns='FooElement'
                     ))]
    )]


def test_empty_interface():
    actual = ingest("interface Foo {\n}")[0]
    assert actual == GInterface('Foo')
    assert actual.to_python() == 'class Foo: ...'


def test_complete_interface():
    actual = ingest("interface Doc : Blob  { attribute Blob baz; } ")[0]

    attr = GAttribute('baz', 'Blob')
    assert actual == GInterface('Doc', bases=['Blob'], body=[attr])
    assert actual.to_python() == 'class Doc(Blob):\n    ' + attr.to_python()


def test_merge():
    piece1 = ingest('interface Doc : Blob  { attribute Blob foo; }')
    piece2 = ingest('partial interface Doc  { attribute Element bar; }')

    expected = ingest('interface Doc : Blob {  attribute Blob foo; attribute Element bar; }')

    actual = merge(piece1 + piece2)
    assert actual == expected


def test_discard_unhandled():
    input = [GUnhandled('un1'),
             GInterface('Doc', body=[GUnhandled('un2'), GUnhandled('un2'), GAttribute('attr1', 'Blob')])]
    actual = discard_unhandled(input)
    assert actual == [GInterface('Doc', body=[GAttribute('attr1', 'Blob')])]


class Test_root:
    root_unhandled_idl = """
dictionary ConsoleInstanceOptions {
ConsoleInstanceDumpCallback dump;
}
"""

    def test_root_raise(self):
        exception = False
        try:
            ingest(self.root_unhandled_idl)
        except Exception as ex:
            exception = True

        assert exception

    def test_root_unhandled(self):
        actual = ingest(self.root_unhandled_idl, throw=False)
        assert len(actual) == 1
        a = actual[0]
        assert isinstance(a, GUnhandled)
        assert 'dump' in a.body_str


class TestInner:
    inner_unhandled_idl = """
interface ConsoleInstanceOptions {
undefined foo();
ConsoleInstanceDumpCallback <invalid> dump;
}
"""

    def test_inner_raise(self):
        exception = False
        try:
            ingest(self.inner_unhandled_idl)
        except Exception as ex:
            exc = ex
            exception = True

        assert exception
        assert 'dump' in str(exc)

    def test_inner_unhandled(self):
        actual = ingest(self.inner_unhandled_idl, throw=False)
        assert len(actual) == 1
        a = actual[0]
        assert isinstance(a, GInterface)
        a: GInterface
        assert len(a.body) == 2


def _verify_2nd_level_construct(idl, expected_python, expected_model):
    actual_model = _2nd_level_construct(idl)
    assert actual_model is not None
    assert actual_model == expected_model
    assert actual_model.to_python() == expected_python


def _2nd_level_construct(idl_piece: str, throw=True) -> GMethod | GAttribute | None:
    parser = widlparser.Parser()
    idl = 'interface DummyInterface {\n' + idl_piece + '\n}'
    parser.parse(idl)
    construct = parser.constructs[0]
    g = i_construct(construct, throw)
    assert isinstance(g, GInterface)
    if len(g.body) == 1:
        return g.body[0]
    return None
