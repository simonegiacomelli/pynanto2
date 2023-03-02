from js import document

from app.browser.d3helpers import d3_load


async def main():
    document.body.innerHTML = ''
    # SillyWidget().append_to(document.body)
    await d3_load.load_d3()

    from remote.widgets.silly_widget import SillyWidget
    from remote.widgets.usecase02.UseCase02_Widget import UseCase02_Widget
    UseCase02_Widget().append_to(document.body)
