from js import document
from pynanto.remote.widgets.filesystem_tree_widget import FilesystemTreeWidget


async def main():
    document.body.innerHTML = ''

    for i in range(10):
        document.body.innerHTML += '<div>ciao</ciao>'

    FilesystemTreeWidget().append_to(document.body)

