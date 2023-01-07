import importlib.util
from types import ModuleType

import pynanto
from pynanto import Routes, Webserver
from pynanto.rpc import Module, RpcRequest, Services
from pynanto.server import find_port
from pynanto_test import for_all_webservers
from pynanto_test.test_rpc import support1, support3
from pynanto_test.test_rpc import support2
from pynanto_test.test_unsync import unsync

support2_module_name = 'pynanto_test.test_rpc.support2'


def test_module_module():
    # WHEN
    target = Module(support1)

    # THEN
    assert target.name == 'pynanto_test.test_rpc.support1'
    assert len(target.functions) == 2


def test_module_function0():
    # WHEN
    target = Module(support1)

    # THEN
    fun = target.functions[0]
    assert fun.name == 'support1_function0'
    assert fun.signature == '(a: int, b: int) -> int'
    assert not fun.is_coroutine_function


def test_module_function1():
    # WHEN
    target = Module(support1)

    # THEN
    fun = target.functions[1]
    assert fun.name == 'support1_function1'
    assert fun.signature == '(a: int, b: float) -> str'
    assert fun.is_coroutine_function


def test_module_getitem_and_invoke():
    target = Module(support2)

    # THEN
    actual = target['support2_mul'].func(6, 7)
    assert actual == 42


@unsync
async def test_module_invoke_async():
    target = Module(support2)

    # THEN
    function = target['support2_concat']
    assert function.is_coroutine_function
    actual = await function.func('hello', ' world')
    assert actual == 'hello world'


def test_rpc():
    request = RpcRequest.build_request(support2_module_name, 'support2_mul', 6, 7)
    restored = RpcRequest.from_json(request.json())

    assert restored.module == support2_module_name
    assert restored.func == 'support2_mul'
    assert restored.args == [6, 7]


def test_services_not_found():
    target = Services()
    actual = target.find_module(support2_module_name)
    assert actual is None

    target.add_module(Module(support2))
    actual = target.find_module(support2_module_name)
    assert actual is not None
    actual: Module
    assert actual.name == support2_module_name


@for_all_webservers()
def test_rpc_integration(webserver: Webserver):
    """ server part """
    services = Services()
    module = Module(support3)
    services.add_module(module)

    webserver.set_routes(Routes().add_route_obj(services.route))
    webserver.set_port(find_port()).start_listen().wait_ready()

    rpc_url = webserver.localhost_url() + services.route.path
    imports = 'from pynanto.server.fetch import async_fetch_str'
    stub_source = pynanto.rpc.generate_stub_source(module, rpc_url, imports)
    """ end """

    """ client part """
    client_module = _module_from_source('dynamic_module', stub_source)

    @unsync
    async def verify():
        target = await client_module.support3_mul(3, 4)
        assert target == 12

        target = await client_module.support3_concat('foo', 'bar')
        assert target == 'foobar'

        target = await client_module.support3_with_typing_import()
        assert target == {'foo': 'bar'}  # this could fail do to missing 'from typing import Dict'

    verify()
    """ end """


def _module_from_source(name: str, source: str) -> ModuleType:
    spec = importlib.util.spec_from_loader(name, loader=None)
    module = importlib.util.module_from_spec(spec)
    exec(source, module.__dict__)
    return module
