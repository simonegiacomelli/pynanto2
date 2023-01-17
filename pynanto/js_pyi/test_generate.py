from js_pyi.generate import *


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
    g_name = GName('DOMString')
    g_arguments = GArguments(args=[GArg('localName', g_name)])
    g_function_def = GFunctionDef('createElement', arguments=g_arguments, returns=GName('FooElement'))
    g_class_def = GClassDef('Document', bases=['Node'], body=[g_function_def])
    actual0 = actual[0]
    assert actual0 == g_class_def
