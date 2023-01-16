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

    async def btn1__click(self, event):
        # document.body.innerHTML = 'ciao2'
        from js import navigator

        opt = to_js(
            {
                # 'acceptAllDevices': True,
                'optionalServices': [0x1800, 0x1801, SERVICE],
                'filters': [
                    {'namePrefix': 'Car'}
                ]
            }
        )
        device = await navigator.bluetooth.requestDevice(opt)
        console.log(device)
        server = await device.gatt.connect()

        print('server.getPrimaryService(SERVICE)...')
        serviceSensors = await server.getPrimaryService(SERVICE)
        self.serviceSensors = serviceSensors
        print('getCharacteristic(READ_PACKET)...')
        characteristic = await serviceSensors.getCharacteristic(READ_PACKET)
        # print('getCharacteristic(WRITE_PACKET)...')
        self.write_packet_char = await serviceSensors.getCharacteristic(WRITE_PACKET)
        characteristic.addEventListener(
            'characteristicvaluechanged',
            create_proxy(self.valueChanged),
            to_js({'capture': True})
        )
        print('startNotifications()...')
        await characteristic.startNotifications()
        print('startNotifications() done')

    async def write_packet(self, packet_bytes):
        await self.write_packet_char.writeValue(packet_bytes)

    async def valueChanged(self, event):
        raw = event.target.value
        str = ''
        for idx in range(raw.byteOffset, raw.byteLength):
            ch = raw.getUint8(idx)
            str += f'{ch:02x}'

        cmd = chr(raw.getUint8(raw.byteOffset))
        print('cmd', cmd, str)
        log = print
        if cmd == 'P':
            log('answering with password')
            from js import TextEncoder
            pass_bytes = TextEncoder.new().encode('PD8GnDV5wkp8BeJ58PJ5')
            await self.write_packet(pass_bytes)
        if cmd == 'M':
            log('answering with sending mode')
            from js import Uint8Array
            new = Uint8Array.new(bytes.fromhex('4D658E'))
            console.log(new)
            await self.write_packet(new)
            # await self.write_packet(bytes([65, 120, 49 + 128, 16, 99, 101 + 128]))
