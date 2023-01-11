from pynanto.remote.widget import Widget

from remote.execute_sql_widget import ExecuteSqlWidget


class SillyWidget(Widget):
    def __init__(self):
        super().__init__(html)
        self.btn1 = self

    def after_render(self):
        async def click(x):
            self.btn1.onclick = None
            ExecuteSqlWidget().append_to(self.container)

        self.btn1.onclick = click


# language=html
html = """
<button id='btn1'>clickme</button>
"""
