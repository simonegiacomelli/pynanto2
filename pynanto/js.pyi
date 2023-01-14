from typing import Any, Callable


class HTMLElement:
    innerHTML: str
    onclick: Any


class Document:
    body: HTMLElement

    def createElement(self, tag: str) -> HTMLElement: ...


class Console:
    def log(self, *args): ...


def setInterval():
    pass


def setTimeout(functionRef: Callable, delay=None, *args):
    pass


class Window: ...


def fetch(url: str, method: str = 'GET', body=None): ...


document: Document
console: Console
window: Window
