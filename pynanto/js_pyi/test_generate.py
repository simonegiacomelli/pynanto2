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
    actual = generate("""
interface Document  {
  Element createElement(DOMString localName, optional (ElementCreationOptions or DOMString) options);
}    
    """)
    assert actual == [GClassDef(
        'Document', body=[
            GFunctionDef('createElement', arguments=(GArguments(args=[
                GArg('localName', 'DOMString'),
                GArg('options', GUnion(['None', 'ElementCreationOptions', 'DOMString']))
            ])), returns='Element')
        ]
    )]


def test_optional_with_default():
    actual = generate("""
interface Document  {
    Node importNode(Node node, optional boolean deep = false);
}    
    """)
    assert actual == [GClassDef(
        'Document', body=[
            GFunctionDef('importNode', arguments=(GArguments(args=[
                GArg('node', 'Node'),
                GArg('deep', GUnion(['None', 'bool']), default='False')
            ])), returns='Node')

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
