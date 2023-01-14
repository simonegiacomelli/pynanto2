from js import document

from remote.pn_button import PnButton


async def main():
    # import os
    document.body.innerHTML = 'ciaoo3'

    btn = PnButton()

    async def btn_click(event):
        print('ok')

    btn.onclick = btn_click
    # from js import window
    # window.pyodide \
    #         await pyodide.loadPackage("micropip");
    # print('import ok')
