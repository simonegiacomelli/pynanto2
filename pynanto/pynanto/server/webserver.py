from pynanto.common import Webserver


def flask() -> Webserver:
    import ws_flask
    return ws_flask.WsFlask()
