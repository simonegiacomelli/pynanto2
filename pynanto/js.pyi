class HTMLElement:
    innerHTML: str
    onclick: Any


class Document:
    body: HTMLElement

    def createElement(self, tag: str) -> HTMLElement: ...


class Console: ...


def fetch(url: str, method: str = 'GET', body=None): ...


document: Document
console: Console
