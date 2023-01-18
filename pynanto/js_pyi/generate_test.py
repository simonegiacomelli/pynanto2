from js_pyi.g_dataclasses import *


def test_attribute():
    actual = repr(GAttribute('implementation', annotation='DOMImplementation'))
    assert actual == 'implementation: DOMImplementation'


def test_method_1():
    actual = repr(GMethod('foo', arguments=(GArguments(args=[])), returns='undefined'))
    assert actual == 'def foo(): ...'


def test_method_2():
    actual = repr(GMethod('foo', arguments=(GArguments(args=[])), returns='DOMString'))
    assert actual == 'def foo() -> str: ...'


def test_method_3():
    actual = repr(GMethod('foo', arguments=(GArguments(args=[
        GArg('localName', 'DOMString'),
        GArg('node', 'Node'),
    ])), returns='undefined'))
    assert actual == 'def foo(localName: str, node: Node): ...'
