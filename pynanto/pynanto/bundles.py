from pathlib import Path
from typing import List, Optional

from pynanto.bundle import Bundle
from pynanto.bundle import strategy_no_cache, ResourceGenerator, LambdaBundle
from pynanto.common.bundle import bundle_definition
from pynanto.resource import StringResource
from pynanto.response import Response


class Bundles:
    def __init__(self):
        self.list: List[Bundle] = []
        self.strategy = strategy_no_cache

    def to_response(self) -> Response:
        return Response.application_zip(self.strategy(self.list))

    def add_resources(self, items: ResourceGenerator):
        self.list.append(LambdaBundle(items))

    def add_flat_folder(self, folder: Path, relative_to: Optional[Path] = None):
        self.add_resources(lambda: bundle_definition(folder, relative_to=relative_to))

    def add_file_content(self, filename: str, content: str):
        resource_list = [StringResource(filename, content)]
        self.list.append(LambdaBundle(lambda: resource_list))
