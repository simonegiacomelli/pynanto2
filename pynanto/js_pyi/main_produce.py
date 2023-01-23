from js_pyi.clipboard import clip_copy
from js_pyi.produce import produce


def main():
    code = _head + produce() + _tail
    print(code)
    clip_copy(code)


_head = """# @formatter:off

from typing import Awaitable, Sequence, Literal, overload
USVString = str


"""
_tail = """

document: Document
window: Window
navigator: Navigator

"""
if __name__ == '__main__':
    main()
