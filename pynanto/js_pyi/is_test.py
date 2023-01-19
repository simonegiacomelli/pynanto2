"""ingest and stringify tests"""
from __future__ import annotations

import widlparser

from js_pyi.datamodel import *
from js_pyi.ingest import ingest, i_construct


def test_nullable():
    _verify_2nd_level_construct(
        'undefined bar (DOMString? name);',
        'def bar(self, name: str | None): ...',
        GMethod('bar', [GArg('name', GOptional('DOMString'))], 'undefined')
    )


def test_method_no_params():
    _verify_2nd_level_construct(
        'undefined foo();',
        'def foo(self): ...',
        GMethod('foo', returns='undefined'),
    )


def test_optional_with_default():
    _verify_2nd_level_construct(
        'undefined time(optional DOMString label = "foobar");',
        'def time(self, label: str = "foobar"): ...',
        GMethod('time', [GArg('label', 'DOMString', '"foobar"', optional=True)], 'undefined')
    )


def test_attribute():
    _verify_2nd_level_construct(
        'attribute DOMImplementation xyz;',
        'xyz: DOMImplementation',
        GAttribute('xyz', 'DOMImplementation'),
    )


def test_compound_nullable():
    _verify_2nd_level_construct(
        'undefined foo( (HTMLElement or long)? before );',
        'def foo(self, before: HTMLElement | int | None): ...',
        GMethod('foo', [GArg('before', GOptional(GUnion(['HTMLElement', 'long'])))], 'undefined')
    )


def test_compound_nullable_optional_default():
    _verify_2nd_level_construct(
        'undefined foo( optional (HTMLElement or long)? before = null);',
        'def foo(self, before: HTMLElement | int | None = None): ...',
        GMethod('foo', [
            GArg('before', GOptional(GUnion(['HTMLElement', 'long'])), 'null', optional=True)
        ], 'undefined'),
    )


def test_interface():
    actual = ingest("""
interface Document : Node {
FooElement createElement(DOMString localName);
}    
""")

    assert actual == [GInterface(
        'Document', bases=['Node'], body=[
            (GMethod('createElement', arguments=[GArg('localName', 'DOMString')],
                     returns='FooElement'
                     ))]
    )]


def test_optionals_no_default():
    idl = "Element createElement(DOMString localName, optional (ElementCreationOptions or DOMString) options);"
    actual = _2nd_level_construct(idl)
    assert actual == GMethod('createElement', arguments=[
        GArg('localName', 'DOMString'),
        GArg('options', GUnion(['ElementCreationOptions', 'DOMString']), optional=True)
    ], returns='Element')

    return
    assert actual.as_python() == (
        'def createElement(self, localName: str, '
        'options: ElementCreationOptions | str | None = None) -> Element: ...')


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
        assert 'dump' in a.body


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
    assert actual_model == expected_model
    assert actual_model.as_python() == expected_python


def _2nd_level_construct(idl_piece: str) -> GMethod | GAttribute:
    parser = widlparser.Parser()
    idl = 'interface DummyInterface {\n' + idl_piece + '\n}'
    parser.parse(idl)
    construct = parser.constructs[0]
    g = i_construct(construct, True)
    assert isinstance(g, GInterface)
    assert len(g.body) == 1
    return g.body[0]
