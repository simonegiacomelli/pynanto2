from js import document
from pynanto.remote.widget import Widget


class PnButton:

    def __init__(self):
        w = Widget("<button>button1</button>")
        self._proxy = w.container.firstChild
        # self._proxy.innerHTML = 'button'
        document.body.append(w.container)

    def __getattr__(self, attr):
        if attr == '_proxy':
            return self._proxy
        return getattr(self._proxy, attr)

    def __setattr__(self, key, value):
        if key == '_proxy':
            super().__setattr__(key, value)
        else:
            setattr(self._proxy, key, value)
