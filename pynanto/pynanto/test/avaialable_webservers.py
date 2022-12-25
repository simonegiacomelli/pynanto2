class AvailableWebservers:
    def __init__(self):
        self.classes = _webservers_classes()
        self.ids = map(lambda w: w.__name__, _webservers_classes())


def _webservers_classes():
    result = []
    try:
        from pynanto.webserver.fastapi import WsFastapi
        result.append(WsFastapi)
    except:
        pass
    try:
        from pynanto.webserver.flask import WsFlask
        result.append(WsFlask)
    except:
        pass

    return result


available_webservers = AvailableWebservers()
