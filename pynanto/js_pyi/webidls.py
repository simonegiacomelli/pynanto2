from pathlib import Path


def find(filename: str) -> Path:
    root = Path(__file__).parent / 'webidls'
    folders = 'enabled unstable unavailable_option_primitive'.split(' ')

    for path in map(lambda s: root / s, folders):
        files = path.glob('*.webidl')
        for file in files:
            if file.name == filename:
                return file
    raise Exception(f'not found: `{file}`')
