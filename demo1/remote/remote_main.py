import datetime

from js import document

from remote.execute_sql_widget import ExecuteSqlWidget
from server.rpc import server_list_dir, server_execute_sql


async def main():
    directories = await server_list_dir('/')
    document.body.innerHTML = f'ciao {datetime.datetime.now()}<br>{directories}'
    btn = document.createElement('button')
    btn.innerHTML = 'clickme'
    div = document.createElement('div')
    div.innerHTML = 'loading'

    async def click(x):
        result = await server_execute_sql('select * from rp_clienti')
        div.innerHTML = str(result)

    btn.onclick = click
    document.body.append(btn)
    document.body.append(div)

    ExecuteSqlWidget().append_to(document.body)
