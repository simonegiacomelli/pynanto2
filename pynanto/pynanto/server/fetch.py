import urllib
import urllib.request

from pynanto import Response


def js_fetch_str(url: str, method: str = 'GET', body: str = '') -> str:
    with urllib.request.urlopen(url) as r:
        return r.read().decode("utf-8")


def sync_fetch_response(url: str, method: str = 'GET', data: str = '') -> Response:
    def make_response(r):
        return Response(
            r.read().decode("utf-8"),
            r.headers.get_content_type()
        )

    if method != 'GET':
        if isinstance(data, str):
            data = bytes(data, 'utf8')
        rq = urllib.request.Request(url, method=method, data=data)
        with urllib.request.urlopen(rq) as r:
            return make_response(r)
    else:
        with urllib.request.urlopen(url) as r:
            return make_response(r)
