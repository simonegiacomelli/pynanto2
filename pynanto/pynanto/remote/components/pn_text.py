from js import document
from pynanto.remote.components.ForwardTo import forward_to


class PnText:

    def __init__(self, text=None):
        div = document.createElement("div")
        if text is not None:
            div.innerHTML = text
        self._proxy = div
        document.body.append(div)


forward_to(PnText, '_proxy')
