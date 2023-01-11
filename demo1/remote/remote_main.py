from js import document

from remote.widgets.silly_widget import SillyWidget


async def main():
    document.body.innerHTML = ''
    SillyWidget().append_to(document.body)
