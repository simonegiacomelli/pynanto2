"""ingest and stringify tests"""
from __future__ import annotations

from js_pyi.assertions import expect_isinstance
from js_pyi.datamodel import *
from js_pyi.datamodel import GPythonProducer
from js_pyi.ingest import ingest, keep_python_producer


def test_attribute():
    _verify_interface_stmt(
        'attribute Blob foo;',
        'foo: Blob',
        GAttribute('foo', 'Blob'),
    )


generics_webidl = [
    ('Promise', 'Awaitable'),
    ('sequence', 'Sequence')
]


def test_generic_attribute():
    for gen, pyt in generics_webidl:
        _verify_interface_stmt(
            f'attribute {gen}<Blob> foo;',
            f'foo: {pyt}[Blob]',
            GAttribute('foo', GGeneric(gen, 'Blob')),
        )


def test_generic_attribute_undefined():
    _verify_interface_stmt(
        'Promise<undefined> abort();',
        f'def abort(self) -> Awaitable[None]: ...',
        GMethod('abort', returns=GGeneric('Promise', 'undefined')),
    )


def test_generic_method_parameter():
    for gen, pyt in generics_webidl:
        _verify_interface_stmt(
            f'Blob foo ((Rest or {gen}<Flip>) bar);',
            f'def foo(self, bar: Rest | {pyt}[Flip]) -> Blob: ...',
            GMethod('foo', [GArg('bar', ['Rest', GGeneric(gen, 'Flip')])],
                    returns='Blob'),
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


def test_interface_mixin():
    idl = 'interface mixin Foo {\n  attribute OnErrorEventHandler onerror; Flip foo(); \n }; '
    stmt = _root_stmt(idl, throw=True)
    expect_isinstance(stmt, GClass)


def test_include():
    _verify_root_stmt('Foo includes Bar', '', GInclude('Foo', 'Bar'))


def test_typedef():
    _verify_root_stmt(
        'typedef Blob Foo;',
        'Foo = Blob',
        GTypedef('Foo', 'Blob'),
    )

    _verify_root_stmt(
        'typedef (Blob or Element) Foo;',
        'Foo = Blob | Element',
        GTypedef('Foo', ['Blob', 'Element']),
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
    actual_model = _root_stmt('nonexistent_type Foo ;', throw=False)
    assert GUnhandledRoot == type(actual_model)


def test_unsupported__attribute_names():
    idl = 'attribute object global;'
    actual_model = _interface_stmt(idl, throw=False)
    assert GUnhandledNested == type(actual_model)

    idl = 'attribute object as;'
    actual_model = _interface_stmt(idl, throw=False)
    assert GUnhandledNested == type(actual_model)


def test_unsupported__comments():
    idl = 'Blob foo(optional Blob bar = 0  /* comment */ );'
    actual_model = _interface_stmt(idl, throw=False)
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
    actual = ingest(
        "interface Document : Blob {\n"
        "FooElement createElement(DOMString localName);\n"
        "}"
    )

    assert actual == [GClass('Document', bases=['Blob'], children=[
        (GMethod('createElement',
                 arguments=[GArg('localName', 'DOMString')],
                 returns='FooElement'))]
                             )]


def test_empty_interface_with_constructor():
    _verify_root_stmt(
        '[Constructor]\ninterface Foo {\n}',
        'class Foo: ...',
        GClass('Foo', children=[GIgnoredStmt(body_str='Constructor')])
    )


def test_complete_interface():
    _verify_root_stmt(
        'interface Doc : Blob  { attribute Blob baz; } ',
        'class Foo:\n    baz: Blob',
        GClass('Doc', bases=['Blob'], children=[(GAttribute('baz', 'Blob'))])
    )


def _append_base(cl: GClass, base: str):
    expect_isinstance(cl, GClass)
    cl.bases.append(base)


def test_keep_python_producer():
    stmts = [GUnhandled('un1'),
             GClass('Doc', children=[GUnhandled('un2'), GUnhandled('un2'), GAttribute('attr1', 'Blob')])]
    actual = keep_python_producer(stmts)
    assert actual == [GClass('Doc', children=[GAttribute('attr1', 'Blob')])]


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
    expect_isinstance(a, GClass)
    a: GClass
    assert len(a.children) == 2


def _verify_interface_stmt(idl, expected_python, expected_model):
    actual = _interface_stmt(idl)
    assert actual is not None
    assert actual == expected_model
    assert actual.to_python() == expected_python


def _verify_root_stmt(idl, expected_python, expected):
    actual = _root_stmt(idl, throw=True)
    assert actual == expected
    if expected is GPythonProducer:
        assert actual.to_python() == expected_python


def _interface_stmt(idl_piece: str, throw=True) -> GMethod | GAttribute | None:
    idl = 'interface Dummy {\n' + idl_piece + '\n}'
    stmt = _root_stmt(idl, throw)
    expect_isinstance(stmt, GClass)
    if len(stmt.children) == 1:
        return stmt.children[0]
    return None


def _root_stmt(idl, throw=True) -> GRootStmt:
    sts = ingest(idl, throw=throw)
    assert len(sts) == 1
    st = sts[0]
    o_type = GRootStmt
    expect_isinstance(st, o_type)
    return st
