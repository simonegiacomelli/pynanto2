import widlparser
from widlparser import Construct

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
    idl = 'undefined enableStyleSheetsForSet (DOMString? name);'
    actual = _single_construct(idl)
    assert actual == GMethod('enableStyleSheetsForSet', arguments=[
        GArg('name', annotation=GNullable('DOMString'))
    ], returns='undefined')


def test_compound_nullable():
    idl = 'undefined foo( (HTMLElement or long)? before );'
    actual = _single_construct(idl)
    assert actual == GMethod('foo', arguments=[
        GArg('before', annotation=GNullable(GUnion(['HTMLElement', 'long'])))
    ], returns='undefined')


def test_compound_nullable_optional_default():
    idl = 'undefined foo( optional (HTMLElement or long)? before = null);'
    actual = _single_construct(idl)
    assert actual == GMethod('foo', arguments=[
        GArg('before', annotation=GNullable(GUnion(['HTMLElement', 'long'])),
             default='null',
             optional=True
             )
    ], returns='undefined')


def test_attribute():
    idl = 'readonly attribute DOMImplementation implementation;'
    actual = _single_construct(idl)
    assert actual == GAttribute('implementation', annotation='DOMImplementation')


unhandled_idl = """
dictionary ConsoleInstanceOptions {
  ConsoleInstanceDumpCallback dump;
}
"""


def test_raise():
    exception = False
    try:
        ingest(unhandled_idl)
    except Exception as ex:
        exception = True

    assert exception


def test_unhandled():
    actual = ingest(unhandled_idl, throw=False)
    assert len(actual) == 1
    a = actual[0]
    assert isinstance(a, GUnhandled)
    assert 'dump' in a.body


def _single_construct(idl_piece: str) -> Construct:
    parser = widlparser.Parser()
    idl = 'interface DummyInterface {\n' + idl_piece + '\n}'
    parser.parse(idl)
    construct = parser.constructs[0]
    g = i_construct(construct)
    assert isinstance(g, GInterface)
    assert len(g.body) == 1
    return g.body[0]
