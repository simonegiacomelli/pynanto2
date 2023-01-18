from js_pyi.g_dataclasses import *


def test_attribute():
    actual = repr(GAttribute('implementation', annotation='DOMImplementation'))
    assert actual == 'implementation: DOMImplementation'


def test_method1():
    actual = repr(GMethod('foo', arguments=(GArguments(args=[])), returns='undefined'))
    assert actual == 'def foo(): ...'
