from pynanto.rpc import Introspection
from pynanto_test.test_rpc import support1
from pynanto_test.test_rpc import support2


def test_introspection_module():
    # WHEN
    target = Introspection(support1)

    # THEN
    assert target.name == 'pynanto_test.test_rpc.support1'
    assert len(target.functions) == 2


def test_introspection_function0():
    # WHEN
    target = Introspection(support1)

    # THEN
    fun = target.functions[0]
    assert fun.name == 'support1_function0'
    assert fun.signature == '(a: int, b: int) -> int'
    assert not fun.is_coroutine_function


def test_introspection_function1():
    # WHEN
    target = Introspection(support1)

    # THEN
    fun = target.functions[1]
    assert fun.name == 'support1_function1'
    assert fun.signature == '(a: int, b: float) -> str'
    assert fun.is_coroutine_function


def test_introspection_getitem_and_invoke():
    target = Introspection(support2)

    # THEN
    actual = target['support2_mul'].func(6, 7)
    assert actual == 42


async def test_introspection_invoke_async():
    target = Introspection(support2)

    # THEN
    function = target['support2_async']
    assert function.is_coroutine_function
    actual = await function.func('hello', ' world')
    assert actual == 'hello world'
