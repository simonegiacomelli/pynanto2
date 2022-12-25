from typing import List, Callable, NamedTuple

from pynanto import Response


class Route(NamedTuple):
    path: str
    callback: Callable[[], Response]


class Routes:
    def __init__(self):
        self.list: List[Route] = []

    def add_root_index(self) -> 'Routes':
        return self

    def add_route(self, path: str, callback: Callable[[], Response]) -> 'Routes':
        self.list.append(Route(path, callback))
        return self

    @property
    def is_empty(self) -> bool:
        return len(self.list) == 0
