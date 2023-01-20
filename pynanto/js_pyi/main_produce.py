from js_pyi.clipboard import clip_copy
from js_pyi.produce import produce


def main():
    code = produce()
    print(code)
    clip_copy(code)


if __name__ == '__main__':
    main()
