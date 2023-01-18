from js_pyi.g_dataclasses import *
from js_pyi.generate import generate


def test_simple():
    actual = generate("""
interface Document : Node {
  FooElement createElement(DOMString localName);
}    
    """)

    assert actual == [GInterface(
        'Document', bases=['Node'], body=[
            (GMethod('createElement', arguments=(GArguments(args=[GArg('localName', 'DOMString')])),
                     returns='FooElement'
                     ))]
    )]


def test_optionals():
    actual = generate("""
interface Document  {
  Element createElement(DOMString localName, optional (ElementCreationOptions or DOMString) options);
}    
    """)
    g_union = GUnion(['ElementCreationOptions', 'DOMString'])
    g_optional = GOptional(g_union)
    assert actual == [GInterface(
        'Document', body=[
            GMethod('createElement', arguments=(GArguments(args=[
                GArg('localName', 'DOMString'),
                GArg('options', g_optional)
            ])), returns='Element')
        ]
    )]


def test_optional_with_default():
    actual = generate("""
interface ConsoleInstance  {
    undefined time(optional DOMString label = "foobar");
}    
    """)
    assert actual == [GInterface(
        'ConsoleInstance', body=[
            GMethod('time', arguments=(GArguments(args=[
                GArg('label', GOptional('DOMString'), default='"foobar"')
            ])), returns='undefined')

        ])]


def test_attribute():
    actual = generate("""
interface Document  {
  readonly attribute DOMImplementation implementation;
}    
    """)
    assert actual == [GInterface(
        'Document', body=[
            GAttribute('implementation', annotation='DOMImplementation')
        ])]


unhandled_idl = """
dictionary ConsoleInstanceOptions {
  ConsoleInstanceDumpCallback dump;
}
"""


def test_raise():
    exception = False
    try:
        generate(unhandled_idl)
    except Exception as ex:
        exception = True

    assert exception


def test_unhandled():
    actual = generate(unhandled_idl, throw=False)
    assert len(actual) == 1
    a = actual[0]
    assert isinstance(a, GUnhandled)
    assert 'dump' in a.body
