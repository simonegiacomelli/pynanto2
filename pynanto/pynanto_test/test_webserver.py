import urllib
import urllib.request

from pynanto import Response, Routes, Webserver
from pynanto.server import find_port
from pynanto_test import for_all_webservers


@for_all_webservers()
def test_webserver_implementations(webserver: Webserver):
    response_a = Response('a', 'text/plain')
    response_b = Response('b', 'text/plain')

    routes = (
        Routes()
        .add_route('/b', lambda: response_b)
        .add_route('/', lambda: response_a)
    )

    webserver.set_routes(routes).set_port(find_port()).start_listen().wait_ready()

    url = webserver.localhost_url()

    assert get_url_response(url) == response_a
    assert get_url_response(url + '/b') == response_b


def get_url_response(url: str) -> Response:
    with urllib.request.urlopen(url) as r:
        return Response(
            r.read().decode("utf-8"),
            r.headers.get_content_type()
        )
