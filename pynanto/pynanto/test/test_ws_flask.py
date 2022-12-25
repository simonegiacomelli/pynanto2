import unittest
import urllib
import urllib.request

import pynanto
import pynanto.server.wait_url
from pynanto import Routes, Response
from pynanto.flask import WsFlask
from pynanto.server.find_port import find_port


class MyTestCase(unittest.TestCase):
    def test_something(self):
        response = Response('<h1>hello</h1>', 'text/html')

        def callback():
            return response

        routes = Routes().add_route('/', callback)

        port = find_port()
        ws = WsFlask()

        ws \
            .set_routes(routes) \
            .set_host('0.0.0.0') \
            .set_port(port) \
            .start_listen()

        url = f'http://127.0.0.1:{port}'
        pynanto.server.wait_url.wait_url(url + '/is_server_running')

        actual = get_url_response(url)

        self.assertEqual(response, actual)


def get_url_response(url: str) -> Response:
    with urllib.request.urlopen(url) as r:
        return Response(
            r.read().decode("utf-8"),
            r.headers.get_content_type()
        )


if __name__ == '__main__':
    unittest.main()
