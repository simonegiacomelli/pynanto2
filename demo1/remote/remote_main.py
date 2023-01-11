import datetime

from js import document

from remote.execute_sql_widget import ExecuteSqlWidget


async def main():
    # directories = await server_list_dir('/')
    document.body.innerHTML = f'ciao {datetime.datetime.now()}<br><br><br>'
    btn = document.createElement('button')
    btn.innerHTML = 'clickme'

    async def click(x):
        btn.onclick = None
        ExecuteSqlWidget().append_to(document.body)

    btn.onclick = click
    document.body.append(btn)


