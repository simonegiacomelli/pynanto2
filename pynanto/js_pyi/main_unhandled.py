from js_pyi.produce import unhandled
from js_pyi.webidls import find


def main():
    unhandled([find('Document.webidl')])


if __name__ == '__main__':
    main()
