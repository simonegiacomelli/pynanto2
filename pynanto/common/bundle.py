import glob
from collections import namedtuple
from os import PathLike
from pathlib import Path
from typing import Iterator, Tuple, Union, NamedTuple, Optional, Callable


class Item(NamedTuple):
    filepath: Path
    arcname: str


def default_item_filter(item: Item) -> Optional[Item]:
    filepath = item.filepath
    if filepath.name == '.DS_Store':
        return None
    if filepath.name == '__pycache__' and filepath.is_dir():
        return None
    return item


def bundle_definition(folder: Path, relative_to: Optional[Path] = None
                      , item_filter: Callable[[Item], Optional[Item]] = default_item_filter) -> Iterator[Item]:
    if relative_to is None:
        relative_to = folder

    def recurse(path: Path):
        for f in path.glob('*'):
            rel = f.relative_to(relative_to)
            candidate = Item(f, str(rel))
            item = item_filter(candidate)
            if item is not None:
                if f.is_file():
                    yield item
                else:
                    yield from recurse(f)

    yield from recurse(folder)
    return iter(())
