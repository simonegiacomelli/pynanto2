import pynanto as pn


def main():
    cfg = pn.Config().quickstart()
    cfg.webserver.start_listen()
    pn.wait_forever()


if __name__ == '__main__':
    main()
