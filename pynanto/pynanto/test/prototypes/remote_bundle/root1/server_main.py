from time import sleep

import pynanto as pn


def main():
    cfg = pn.Config().quickstart()
    cfg.webserver.start_listen()

    while True:
        sleep(10)


if __name__ == '__main__':
    main()
