from typing import List

from pynanto import Resource, StringResource


class Bundle:
    def __init__(self):
        self.list: List[Resource] = []

    def add_file_content(self, filename: str, content: str):
        self.list.append(StringResource(filename, content))
