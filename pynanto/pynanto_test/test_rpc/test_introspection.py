import asyncio
from threading import Thread

from pynanto.rpc import Introspection, RpcRequest
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


def test_introspection_invoke_async():
    async def main():
        target = Introspection(support2)

        # THEN
        function = target['support2_concat']
        assert function.is_coroutine_function
        actual = await function.func('hello', ' world')
        assert actual == 'hello world'

    async def main_safe():
        try:
            return await main()
        except Exception as ex:
            return ex

    result = None

    def start():
        nonlocal result
        result = asyncio.run(main_safe())

    thread = Thread(target=start)
    thread.start()
    thread.join()
    if result is not None:
        raise result


def test_rpc():
    callable_path = 'pynanto_test.test_rpc.support2.support2_mul'

    request = RpcRequest.build_request(callable_path, 6, 7)
    restored = RpcRequest.from_json(request.json())

    assert restored.callable_path == callable_path
    assert restored.args == [6, 7]
