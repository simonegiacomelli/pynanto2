"""ingest and stringify tests"""
from __future__ import annotations

from js_pyi.datamodel import *
from js_pyi.ingest import ingest, merge, discard_unhandled


def test_attribute():
    _verify_interface_stmt(
        'attribute Blob foo;',
        'foo: Blob',
        GAttribute('foo', 'Blob'),
    )


def test_method_no_params():
    _verify_interface_stmt(
        'undefined foo();',
        'def foo(self): ...',
        GMethod('foo'),
    )


def test_name_clash_async():
    _verify_interface_stmt(
        'undefined foo (Blob async);',
        'def foo(self, async_: Blob): ...',
        GMethod('foo', [GArg('async', 'Blob')])
    )


def test_nullable():
    _verify_interface_stmt(
        'undefined foo (DOMString? name);',
        'def foo(self, name: str | None): ...',
        GMethod('foo', [GArg('name', ['DOMString', 'None'])])
    )


def test_float():
    _verify_interface_stmt(
        'undefined foo (float x);',
        'def foo(self, x: float): ...',
        GMethod('foo', [GArg('x', 'float')])
    )


def test_enum_root_stmt():
    _verify_root_stmt(
        'enum Foo {"bar","None","class","a-b+c/d", "","2x-y" };',
        'class Foo:\n'
        '    bar = "bar"\n'
        '    None_ = "None"\n'
        '    class_ = "class"\n'
        '    a_b_c_d = "a-b+c/d"\n'
        '    empty_ = ""\n'
        '    X_2x_y = "2x-y"',
        GEnum('Foo', [
            GEnumValue('"bar"'),
            GEnumValue('"None"'),
            GEnumValue('"class"'),
            GEnumValue('"a-b+c/d"'),
            GEnumValue('""'),
            GEnumValue('"2x-y"'),
        ])
    )


def test_root_unhandled():
    actual_model = _root_stmt('nonexistent_type Foo ;')
    assert GUnhandledRoot == type(actual_model)


def test_unsupported__generics():
    idl = 'Blob foo ((Blob or sequence<Blob>) bar);'
    actual_model = _interface_stmt(idl)
    assert GUnhandledNested == type(actual_model)


def test_unsupported__attribute_names():
    idl = 'attribute object global;'
    actual_model = _interface_stmt(idl)
    assert GUnhandledNested == type(actual_model)

    idl = 'attribute object as;'
    actual_model = _interface_stmt(idl)
    assert GUnhandledNested == type(actual_model)


def test_unsupported__comments():
    idl = 'Blob foo(optional Blob bar = 0  /* comment */ );'
    actual_model = _interface_stmt(idl)
    assert GUnhandledNested == type(actual_model)


def test_nullable_result():
    _verify_interface_stmt(
        'Blob? foo();',
        'def foo(self) -> Blob | None: ...',
        GMethod('foo', returns=['Blob', 'None'])
    )


def test_compound_nullable():
    _verify_interface_stmt(
        'undefined foo( (HTMLElement or long)? before );',
        'def foo(self, before: HTMLElement | int | None): ...',
        GMethod('foo', [GArg('before', ['HTMLElement', 'long', 'None'])])
    )


def test_optional():
    _verify_interface_stmt(
        'undefined foo(optional Blob label);',
        'def foo(self, label: Blob | None = None): ...',
        GMethod('foo', [GArg('label', ['Blob', 'None'], 'None')])
    )


def test_optional_with_default():
    _verify_interface_stmt(
        'undefined foo(optional DOMString label = "foobar");',
        'def foo(self, label: str | None = "foobar"): ...',
        GMethod('foo', [GArg('label', ['DOMString', 'None'], '"foobar"')])
    )


def test_compound_nullable_optional_default():
    _verify_interface_stmt(
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


def test_parse_error():
    exception = False
    try:
        ingest('enum InvalidEnum {};')
    except Exception as ex:
        exc = ex
        exception = True

    assert exception
    assert 'SyntaxError' in str(exc)


def test_inner_unhandled():
    inner_unhandled_idl = """
interface ConsoleInstanceOptions {
undefined foo();
attribute Blob global;
}
    """

    actual = ingest(inner_unhandled_idl, throw=False)
    assert len(actual) == 1
    a = actual[0]
    expect_isinstance(a, GInterface)
    a: GInterface
    assert len(a.body) == 2


def _verify_interface_stmt(idl, expected_python, expected_model):
    actual = _interface_stmt(idl)
    assert actual is not None
    assert actual == expected_model
    assert actual.to_python() == expected_python


def _verify_root_stmt(idl, expected_python, expected):
    actual = _root_stmt(idl, throw=True)
    assert actual == expected
    assert actual.to_python() == expected_python


def _interface_stmt(idl_piece: str) -> GMethod | GAttribute | None:
    idl = 'interface Dummy {\n' + idl_piece + '\n}'
    stmt = _root_stmt(idl)
    assert isinstance(stmt, GInterface)
    if len(stmt.body) == 1:
        return stmt.body[0]
    return None


def _root_stmt(idl, throw=False) -> GRootStmt:
    sts = ingest(idl, throw=throw)
    assert len(sts) == 1
    st = sts[0]
    o_type = GRootStmt
    expect_isinstance(st, o_type)
    return st


def expect_isinstance(instance, expected_type):
    if not isinstance(instance, expected_type):
        raise Exception('Expect to find a {expected_type} but found {type(instance)}')
