from pynanto.remote.widget import Widget

from server.rpc import server_execute_sql
from js import console


class ExecuteSqlWidget(Widget):
    def __init__(self):
        super().__init__(html)
        self.id_sql = self
        self.id_btn = self
        self.id_btn = self
        self.id_table = self

    def after_render(self):
        self.id_sql.value = 'select * from rp_clienti'
        self.id_btn.onclick = lambda *args: self._execute_sql()

    async def _execute_sql(self):
        console.log(self.id_sql.value)
        rows = await server_execute_sql(self.id_sql.value)
        t = self.id_table
        t.innerHTML = ''
        body = t.createTBody()
        for row in rows:
            r = body.insertRow(-1)
            for value in row:
                c = r.insertCell()
                c.innerHTML = value


# language=html
html = """
<h1>sql</h1>
<textarea id='id_sql' cols='60' rows='6'></textarea>
<br>
<button id='id_btn'>execute</button>

<table id='id_table'></table>
"""
