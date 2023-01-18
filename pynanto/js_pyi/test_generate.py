from js_pyi.g_dataclasses import *
from js_pyi.generate import generate


def test_simple():
    actual = generate("""
interface Document : Node {
  FooElement createElement(DOMString localName);
}    
    """)

    assert actual == [GClassDef(
        'Document', bases=['Node'], body=[
            (GFunctionDef('createElement', arguments=(GArguments(args=[GArg('localName', 'DOMString')])),
                          returns='FooElement'
                          ))]
    )]


def test_optionals():
    GUnion
    actual = generate("""
interface Document  {
  Element createElement(DOMString localName, optional (ElementCreationOptions or DOMString) options);
}    
    """)
    g_union = GUnion(['ElementCreationOptions', 'DOMString'])
    g_optional = GOptional(g_union)
    assert actual == [GClassDef(
        'Document', body=[
            GFunctionDef('createElement', arguments=(GArguments(args=[
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
    assert actual == [GClassDef(
        'ConsoleInstance', body=[
            GFunctionDef('time', arguments=(GArguments(args=[
                GArg('label', GOptional('DOMString'), default='"foobar"')
            ])), returns='undefined')

        ])]


def test_attribute():
    actual = generate("""
interface Document  {
  readonly attribute DOMImplementation implementation;
}    
    """)
    assert actual == [GClassDef(
        'Document', body=[
            GAttribute('implementation', annotation='DOMImplementation')
        ])]
