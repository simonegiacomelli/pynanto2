import zipfile
from abc import abstractmethod, ABC
from io import BytesIO
from pathlib import Path
from typing import Iterator, Optional, Callable

from attr import dataclass


@dataclass(frozen=True)
class Resource(ABC):
    arcname: str

    @abstractmethod
    def get_content(self) -> str:
        pass


@dataclass(frozen=True)
class PathResource(Resource):
    filepath: Path

    def get_content(self) -> str:
        return self.filepath.read_text()


@dataclass(frozen=True)
class StringResource(Resource):
    content: str

    def get_content(self) -> str:
        return self.content


# class Item(NamedTuple):
#     arcname: str
#     filepath: Path


def default_item_filter(item: Resource) -> Optional[Resource]:
    if not isinstance(item, PathResource):
        return item
    item: PathResource
    filepath = item.filepath
    if filepath.name == '.DS_Store':
        return None
    if filepath.name == '__pycache__' and filepath.is_dir():
        return None
    return item


def bundle_definition(
        folder: Path, relative_to: Optional[Path] = None,
        item_filter: Callable[[PathResource], Optional[PathResource]] = default_item_filter
) -> Iterator[PathResource]:
    if relative_to is None:
        relative_to = folder

    def recurse(path: Path):
        for f in path.glob('*'):
            rel = f.relative_to(relative_to)
            candidate = PathResource(str(rel), f)
            item = item_filter(candidate)
            if item is not None:
                if f.is_file():
                    yield item
                else:
                    yield from recurse(f)

    yield from recurse(folder)
    return iter(())


def build_archive(item_iterator: Iterator[PathResource]) -> bytes:
    stream = BytesIO()
    zf = zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=1)

    for item in item_iterator:
        zf.write(item.filepath, item.arcname)
    zf.close()

    stream.seek(0)
    return stream.getbuffer().tobytes()
