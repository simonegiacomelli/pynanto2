from js_pyi.g_dataclasses import *


def test_attribute():
    actual = GAttribute('implementation', annotation='DOMImplementation').str()
    assert actual == 'implementation: DOMImplementation'


def test_method_1():
    expected = 'def foo(): ...'

    assert expected == GMethod('foo').str()
    assert expected == GMethod('foo', returns='undefined').str()


def test_method_2():
    actual = GMethod('foo', returns='DOMString').str()
    assert actual == 'def foo() -> str: ...'


def test_method_3():
    actual = GMethod('foo', arguments=[
        GArg('localName', 'DOMString'),
        GArg('node', 'Node'),
    ], returns='undefined').str()
    assert actual == 'def foo(localName: str, node: Node): ...'


def test_method_4():
    actual = GMethod('foo', arguments=[
        GArg('name', 'DOMString', '"bar"'),
    ]).str()
    assert actual == 'def foo(name: str = "bar"): ...'
