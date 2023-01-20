from js_pyi.produce import develop
from js_pyi.webidls import find


def main():
    develop([find('Document.webidl')])


if __name__ == '__main__':
    main()
