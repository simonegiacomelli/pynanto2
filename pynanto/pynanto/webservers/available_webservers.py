from pynanto.webserver import Webserver


class AvailableWebservers:
    def __init__(self):
        self.classes = _webservers_classes()
        self.ids = map(lambda w: w.__name__, _webservers_classes())

    def new_instance(self) -> Webserver:
        return self.classes[0]()


def _webservers_classes():
    result = []
    try:
        from pynanto.webservers.fastapi import WsFastapi
        result.append(WsFastapi)
    except:
        pass
    try:
        from pynanto.webservers.flask import WsFlask
        result.append(WsFlask)
    except:
        pass

    return result


_available_webservers = None


def available_webservers() -> AvailableWebservers:
    global _available_webservers
    if _available_webservers is None:
        _available_webservers = AvailableWebservers()
    return _available_webservers
