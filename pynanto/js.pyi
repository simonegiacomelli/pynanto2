from typing import Any, Callable


class Node: ...


class HTMLElement:
    innerHTML: str
    onclick: Any


class Document(Node):
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


def alert(msg: str): ...
