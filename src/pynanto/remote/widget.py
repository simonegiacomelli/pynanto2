import inspect
from typing import TypeVar, Callable

from pyodide.ffi import create_proxy

from js import document, console, HTMLElement

T = TypeVar('T')


class WidgetConstructor:
    def __init__(self, constructor):
        self.constructor = constructor


class Widget:
    def __init__(self, html: str):
        self.html = html
        self._widget_expanded = False
        self._container: HTMLElement = None
        self.holder: HolderWidget = None

    def __call__(self, fun: Callable[[], T]) -> T:
        return WidgetConstructor(fun)

    @property
    def container(self) -> HTMLElement:
        if self._container is None:
            self._container = document.createElement('div')
        self._container.setAttribute('w-type', self.__class__.__name__)
        if not self._widget_expanded:
            self._widget_expanded = True
            self._container.innerHTML = self.html
            self.bind_self_elements()
            self._bind_events()
            self.after_render()

        return self._container

    def append_to(self, container_element):
        container_element.append(self.container)
        return self

    def after_render(self):
        pass

    def bind_self_elements(self):
        def get_binder(value):
            if value == self:
                return lambda element: element
            if isinstance(value, WidgetConstructor):
                def wc_binder(element):
                    instance: Widget = value.constructor()
                    instance._container = element
                    c = instance.container  # force expand
                    return instance

                return wc_binder
            return None

        for key, value in self.__dict__.items():
            binder = get_binder(value)
            if binder is None:
                continue

            element = self.container.querySelector('#' + key)
            if element is None:
                raise Exception(f'Element not found, name:[{key}] html: [{self.html}]')
            instance = binder(element)
            self.__dict__[key] = instance

    def _bind_events(self):

        members = inspect.getmembers(self)

        for name, method in members:
            parts = name.split('__')
            if len(parts) != 2:
                continue

            element_name = parts[0]
            event_name = parts[1]
            if element_name == '' or event_name == '':
                continue

            element = self.container.querySelector('#' + element_name)
            if element is None:
                console.warn(f'Event bind failed, element `{element_name}` was not found for method `{name}`')
                continue

            m = getattr(self, name)
            element.addEventListener(event_name, create_proxy(m))

    def close(self):
        h = self.holder
        if h is not None:
            h.close(self)


class HolderWidget(Widget):
    def __init__(self, html: str = ''):
        super().__init__(html)
        self.stack = []
        self.on_show = lambda w: ...

    def show(self, widget: Widget):
        widget.holder = self
        c = self.container
        while c.hasChildNodes():
            c.removeChild(c.firstChild)

        self._remove(widget)
        self.stack.append(widget)
        widget.append_to(self.container)
        self.on_show(widget)

    def close(self, widget: Widget):
        self._remove(widget)
        self.show(self.stack[-1])

    def _remove(self, widget):
        s = self.stack
        if widget in s:
            s.remove(widget)
