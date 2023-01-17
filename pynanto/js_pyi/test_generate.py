from js_pyi.g_dataclasses import *
from js_pyi.generate import generate


def test_simple():
    idl = """
/* https://dom.spec.whatwg.org/#interface-document */
[Constructor]
interface Document : Node {
  [CEReactions, NewObject, Throws]
  FooElement createElement(DOMString localName);
}    
    """
    actual = generate(idl)
    assert len(actual) == 1

    g_arguments = GArguments(args=[GArg('localName', 'DOMString')])
    g_function_def = GFunctionDef('createElement', arguments=g_arguments, returns='FooElement')
    g_class_def = GClassDef('Document', bases=['Node'], body=[g_function_def])
    actual0 = actual[0]
    assert actual0 == g_class_def


def test_optionals():
    idl = """
/* https://dom.spec.whatwg.org/#interface-document */
[Constructor]
interface Document  {
  [CEReactions, NewObject, Throws]
  Element createElement(DOMString localName, optional (ElementCreationOptions or DOMString) options);
}    
    """
    actual = generate(idl)
    assert len(actual) == 1

    g_arguments = GArguments(args=[
        GArg('localName', 'DOMString'),
        GArg('options', GUnion(['None', 'ElementCreationOptions', 'DOMString']))
    ])
    g_function_def = GFunctionDef('createElement', arguments=g_arguments, returns='Element')
    g_class_def = GClassDef('Document', body=[g_function_def])
    actual0 = actual[0]
    assert actual0 == g_class_def
