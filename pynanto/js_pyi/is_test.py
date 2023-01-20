"""ingest and stringify tests"""
from __future__ import annotations

from js_pyi.datamodel import *
from js_pyi.ingest import ingest, merge, discard_unhandled


def test_attribute():
    _verify_interface_construct(
        'attribute Blob foo;',
        'foo: Blob',
        GAttribute('foo', 'Blob'),
    )


def test_method_no_params():
    _verify_interface_construct(
        'undefined foo();',
        'def foo(self): ...',
        GMethod('foo'),
    )


def test_name_clash_async():
    _verify_interface_construct(
        'undefined foo (Blob async);',
        'def foo(self, async_: Blob): ...',
        GMethod('foo', [GArg('async', 'Blob')])
    )


def test_nullable():
    _verify_interface_construct(
        'undefined foo (DOMString? name);',
        'def foo(self, name: str | None): ...',
        GMethod('foo', [GArg('name', ['DOMString', 'None'])])
    )


def test_float():
    _verify_interface_construct(
        'undefined foo (float x);',
        'def foo(self, x: float): ...',
        GMethod('foo', [GArg('x', 'float')])
    )


def x_test_enum_attribute():
    _verify_root_construct(
        'enum Foo { "bar", "baz" };',
        'class Foo:\n    bar = "bar"',  # \n    baz = "baz"',
        GEnum('foo', [GArg('bar', '', default='"bar"')])
    )


def test_unsupported__generics():
    idl = 'Blob foo ((Blob or sequence<Blob>) bar);'
    actual_model = _interface_construct(idl)
    assert GUnhandledNested == type(actual_model)


def test_unsupported__attribute_names():
    idl = 'attribute object global;'
    actual_model = _interface_construct(idl)
    assert GUnhandledNested == type(actual_model)

    idl = 'attribute object as;'
    actual_model = _interface_construct(idl)
    assert GUnhandledNested == type(actual_model)


def test_unsupported__comments():
    idl = 'Blob foo(optional Blob bar = 0  /* comment */ );'
    actual_model = _interface_construct(idl)
    assert GUnhandledNested == type(actual_model)


def test_nullable_result():
    _verify_interface_construct(
        'Blob? foo();',
        'def foo(self) -> Blob | None: ...',
        GMethod('foo', returns=['Blob', 'None'])
    )


def test_compound_nullable():
    _verify_interface_construct(
        'undefined foo( (HTMLElement or long)? before );',
        'def foo(self, before: HTMLElement | int | None): ...',
        GMethod('foo', [GArg('before', ['HTMLElement', 'long', 'None'])])
    )


def test_optional():
    _verify_interface_construct(
        'undefined foo(optional Blob label);',
        'def foo(self, label: Blob | None = None): ...',
        GMethod('foo', [GArg('label', ['Blob', 'None'], 'None')])
    )


def test_optional_with_default():
    _verify_interface_construct(
        'undefined foo(optional DOMString label = "foobar");',
        'def foo(self, label: str | None = "foobar"): ...',
        GMethod('foo', [GArg('label', ['DOMString', 'None'], '"foobar"')])
    )


def test_compound_nullable_optional_default():
    _verify_interface_construct(
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


def _verify_interface_construct(idl, expected_python, expected_model):
    actual_model = _interface_construct(idl)
    assert actual_model is not None
    assert actual_model == expected_model
    assert actual_model.to_python() == expected_python


def _verify_root_construct(idl, expected_python, expected_model):
    actual_model = _root_construct(idl)
    assert actual_model is not None
    assert actual_model == expected_model
    assert actual_model.to_python() == expected_python


def _interface_construct(idl_piece: str) -> GMethod | GAttribute | None:
    lst = _root_construct('interface Dummy', idl_piece)
    first = lst
    assert isinstance(first, GInterface)
    if len(first.body) == 1:
        return first.body[0]
    return None


def _root_construct(construct_idl, idl_piece='') -> GRootStmt:
    idl = construct_idl + ' {\n' + idl_piece + '\n}'
    sts = ingest(idl, throw=False)
    assert len(sts) == 1
    st = sts[0]
    assert isinstance(st, GRootStmt)
    return st
