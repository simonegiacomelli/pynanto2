from itertools import groupby
from pathlib import Path

from js_pyi.generate import generate


def main():
    webidls_path = Path(__file__).parent / 'webidls'
    txt = ''
    for f in webidls_path.glob('enabled/Document.webidl'):
        print(f'file {f}')
        txt = f.read_text()
        break

    statements = generate(txt, throw=False)
    groupby(statements, )
    for stmt in statements:
        print(stmt)


if __name__ == '__main__':
    main()
