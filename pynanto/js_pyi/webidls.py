from pathlib import Path
from typing import List


def find(filename: str) -> Path:
    for file in _find_all():
        if file.name == filename:
            return file
    raise Exception(f'not found: `{file}`')


def find_all() -> List[Path]:
    return list(_find_all())


def _find_all():
    root = Path(__file__).parent / 'webidls'
    folders = 'enabled unstable unavailable_option_primitive'.split(' ')

    for path in map(lambda s: root / s, folders):
        files = list(path.glob('*.webidl'))
        yield from files
