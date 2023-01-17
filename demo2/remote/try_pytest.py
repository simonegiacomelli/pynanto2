from pathlib import Path

from js import window

import remote.supertyped as st


async def try_pytest():
    async def click(event):
        await window.pyodide.loadPackage("micropip")
        import micropip
        await micropip.install('pytest')
        import pytest

        pytest.main(['-x', str(Path(__file__).resolve().parent)])

    st.button('start pytest', click)
