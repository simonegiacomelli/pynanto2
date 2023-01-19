from js_pyi.clipboard import clip_copy
from js_pyi.produce import produce
from js_pyi.webidls import find


def main():
    code = produce(find('Document.webidl'))
    print(code)
    clip_copy(code)


if __name__ == '__main__':
    main()
