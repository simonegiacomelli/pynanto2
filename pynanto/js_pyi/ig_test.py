from __future__ import annotations

import widlparser

from js_pyi.g_dataclasses import *
from js_pyi.ingest import ingest, i_construct


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


def test_optionals():
    idl = "Element createElement(DOMString localName, optional (ElementCreationOptions or DOMString) options);"
    actual = _single_construct(idl)
    assert actual == GMethod('createElement', arguments=[
        GArg('localName', 'DOMString'),
        GArg('options', GUnion(['ElementCreationOptions', 'DOMString']), optional=True)
    ], returns='Element')


def test_optional_with_default():
    idl = 'undefined time(optional DOMString label = "foobar");'
    actual = _single_construct(idl)
    assert actual == GMethod('time', arguments=[
        GArg('label', 'DOMString', default='"foobar"', optional=True)
    ], returns='undefined')


def test_nullable():
    idl = 'undefined bar (DOMString? name);'
    actual = _single_construct(idl)
    assert actual == GMethod('bar', arguments=[
        GArg('name', annotation=GNullable('DOMString'))
    ], returns='undefined')
    assert actual.str() == "def bar(name: str | None): ..."


def test_compound_nullable():
    idl = 'undefined foo( (HTMLElement or long)? before );'
    actual = _single_construct(idl)
    assert actual == GMethod('foo', arguments=[
        GArg('before', annotation=GNullable(GUnion(['HTMLElement', 'long'])))
    ], returns='undefined')
    assert actual.str() == 'def foo(before: HTMLElement | int | None): ...'


def test_compound_nullable_optional_default():
    idl = 'undefined foo( optional (HTMLElement or long)? before = null);'
    actual = _single_construct(idl)
    assert actual == GMethod('foo', arguments=[
        GArg('before', annotation=GNullable(GUnion(['HTMLElement', 'long'])),
             default='null',
             optional=True
             )
    ], returns='undefined')
    assert actual.str() == "def foo(before: HTMLElement | int | None = None): ..."


def test_attribute():
    idl = 'attribute DOMImplementation xyz;'
    actual = _single_construct(idl)
    assert actual == GAttribute('xyz', annotation='DOMImplementation')
    assert actual.str() == 'xyz: DOMImplementation'


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


def _single_construct(idl_piece: str) -> GMethod | GAttribute:
    parser = widlparser.Parser()
    idl = 'interface DummyInterface {\n' + idl_piece + '\n}'
    parser.parse(idl)
    construct = parser.constructs[0]
    g = i_construct(construct, True)
    assert isinstance(g, GInterface)
    assert len(g.body) == 1
    return g.body[0]
