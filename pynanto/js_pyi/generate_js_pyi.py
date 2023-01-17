from pathlib import Path

from js_pyi.generate import Processor


def main():
    processor = Processor()

    webidls_path = Path(__file__).parent / 'webidls'
    for f in webidls_path.glob('enabled/Document.webidl'):
        print(f'file {f}')
        txt = f.read_text()
        processor.parse(txt)

    print(processor.module)


if __name__ == '__main__':
    main()
