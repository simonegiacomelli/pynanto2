from js import document, window, HTMLElement

from server.rpc import rpc_now
import pynanto.remote.components.supertyped as st


async def main():
    text = st.text("ciaoo")
    res = await rpc_now()
    d = type(res)
    print(f'type(res)={d}')
    text.innerText = f'ciao, type={d} dt={res}'

