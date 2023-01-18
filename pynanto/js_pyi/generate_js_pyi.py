from pathlib import Path

from js_pyi.generate import generate


def main():
    webidls_path = Path(__file__).parent / 'webidls'
    txt = ''
    for f in webidls_path.glob('enabled/Document.webidl'):
        print(f'file {f}')
        txt = f.read_text()
        break

    for stmt in generate(txt):
        print(stmt)


if __name__ == '__main__':
    main()
