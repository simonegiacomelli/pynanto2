from typing import Any

from js import document, console, HTMLElement
from pynanto.remote import to_js
from pynanto.remote.widget import Widget
from pyodide.ffi import create_proxy


async def go_bluetooth():
    document.body.innerHTML = 'loading widget...'
    BluetoothWidget().append_to(document.body)


SERVICE = "195ae58a-437a-489b-b0cd-b7c9c394bae4".lower()
READ_PACKET = "1fde2f31-ba06-47da-9e86-32e3de15e064".lower()
WRITE_PACKET = "26c01ea9-ba06-47da-9e86-32e3de15e777".lower()
SUMMARY_PACKET = "dbcb7b32-2755-11e6-b67b-9e71128cae77".lower()


class BluetoothWidget(Widget):

    def __init__(self):
        super().__init__(
            #     language=html
            """
            <button id='btn1'>bluetooth device dialog</button>
            """
        )

        self.btn1 = self

    async def btn1__click(self, event):
        # document.body.innerHTML = 'ciao2'
        from js import navigator

        opt = to_js({'acceptAllDevices': True})
        device = await navigator.bluetooth.requestDevice(opt)
        console.log(device)
        # devices = await navigator.bluetooth.getDevices()
        # console.log(devices)

