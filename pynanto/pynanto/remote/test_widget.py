import unittest

from js import document, HTMLElement
from pynanto.remote.unittest_fix import unittest_main_fixed
from pynanto.remote.widget import Widget


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
    test_result = unittest_main_fixed(__name__)
    meta = document.createElement('meta')
    meta.name = 'unittest-result'
    meta.content = f'wasSuccessful={test_result.wasSuccessful()}'
    document.head.append(meta)
    # unittest.main()


if __name__ == '__main__':
    main()
