import urllib
import urllib.request

import pynanto
from pynanto import Response, Routes
from pynanto.server import find_port, wait_url


@pynanto.test.for_all_webservers()
def test_webserver_implementations(webserver_class):
    response_a = Response('a', 'text/plain')
    response_b = Response('b', 'text/plain]')

    routes = (
        Routes()
        .add_route('/b', lambda: response_b)
        .add_route('/', lambda: response_a)
    )

    webserver = webserver_class()
    (webserver
     .set_routes(routes)
     .set_binding(('0.0.0.0', find_port()))
     .start_listen()
     )

    url = f'http://127.0.0.1:{webserver.port}'

    wait_url(url + '/is_server_running')

    assert get_url_response(url) == response_a
    assert get_url_response(url + '/b') == response_b


def get_url_response(url: str) -> Response:
    with urllib.request.urlopen(url) as r:
        return Response(
            r.read().decode("utf-8"),
            r.headers.get_content_type()
        )
