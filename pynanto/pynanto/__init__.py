from pathlib import Path
from typing import Union


class Response:
    def __init__(self, content: Union[str, bytes], mimetype: str):
        self.content = content
        self.mimetype = mimetype


class Bootstrap:
    def set_index(self, param) -> 'Bootstrap':
        return self


class Bundle:
    def add_file(self, file: Path) -> 'Bundle':
        return self


class Remote:
    def set_bootstrap(self, bootstrap: Bootstrap) -> 'Remote':
        return self

    def add_bundle(self, bundle: Bundle) -> 'Remote':
        return self

    def set_main(self, script) -> 'Remote':
        return self
