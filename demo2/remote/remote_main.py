from functools import partial

from js import document

from remote.pn_button import PnButton
import remote.supertyped as st
from remote.try_pytest import try_pytest


async def main():
    await try_pytest()
    return
    # import os
    document.body.innerHTML = 'ciaoo3'

    btn = st.button('click me', btn_click)
    sli = st.slider()

async def btn_click(event):
    from js import window
    await window.pyodide.loadPackage("micropip")
    import micropip
    await micropip.install('sqlparse')
    import sqlparse
    print('ok')
    raw = 'select * from foo; select * from bar;'
    statements = sqlparse.split(raw)
    print(statements)
