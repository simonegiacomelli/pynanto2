import unittest

from app.browser.html.dom_definitions import HTMLElement
from app.browser.unittest_fix import unittest_main_fixed
from app.browser.widget.widget import Widget
from js import document, window


class WidgetTestCase(unittest.TestCase):
    def test_basic_bind(self):
        class Widget1(Widget):
            def __init__(self):
                super().__init__("<span id='span1'>foo</span>")
                self.span1: HTMLElement = self
                self.bind_self_elements()

        target = Widget1()
        self.assertEqual('foo', target.span1.innerHTML)

    def test_bind_to_widget(self):
        class WidgetSub(Widget):
            def __init__(self):
                super().__init__("<div>I'm WidgetSub</div>")

        class Widget1(Widget):
            def __init__(self):
                super().__init__("<div id='div1'></div>")
                self.div1 = self(lambda: WidgetSub())

        target = Widget1()
        target.append_to(document.createElement('div'))
        html = target.container.innerHTML
        self.assertTrue("I'm WidgetSub" in html, f'Actual html=```{html}```')

    def test_bind_events(self):
        actual = []

        class Widget1(Widget):
            def __init__(self):
                super().__init__("<button id='foo'>foo</button>")

            def foo__click(self, *args):
                actual.append(1)

        target = Widget1()
        foo = target.container.querySelector('#foo')
        foo.click()
        self.assertEqual([1], actual)


def main():
    unittest_main_fixed(__name__)


if __name__ == '__main__':
    main()
