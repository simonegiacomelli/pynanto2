from typing import List

from pynanto.bundle import Bundle
from pynanto.bundle import strategy_no_cache, ResourceGenerator, LambdaBundle
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

    def add_file_content(self, filename: str, content: str):
        resource_list = [StringResource(filename, content)]
        self.list.append(LambdaBundle(lambda: resource_list))
