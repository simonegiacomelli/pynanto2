from typing import List, Iterable, Callable, Iterator

from pynanto import Resource, StringResource

BundleGenerator = Callable[[], Iterator[Resource]]


class Bundle:
    def __init__(self):
        self._list: List[Resource] = []
        self._iterators: List[BundleGenerator] = []

    def add_file_content(self, filename: str, content: str):
        self._list.append(StringResource(filename, content))

    def add_resources(self, items: BundleGenerator):
        self._iterators.append(items)

    def list(self) -> Iterable[Resource]:
        l_list = self._list.copy()

        yield from l_list
        for i in self._iterators:
            yield from i()
