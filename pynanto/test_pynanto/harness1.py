from time import sleep

if __name__ == '__main__':
    import pynanto
    from pynanto.webserver.flask import WsFlask

    setup = pynanto.Setup().quickstart()
    # setup.bootstrap.set_python(
    #     """from js import document\n"""
    #     """document.body.innerHTML='<input id="tag1" value="Hello world!">'\n"""
    # )
    setup.attach_webserver(WsFlask())
    setup.webserver.set_binding(('0.0.0.0', 8001))
    setup.webserver.start_listen()

    while True:
        sleep(10)
