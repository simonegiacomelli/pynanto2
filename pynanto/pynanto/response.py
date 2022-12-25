from typing import NamedTuple, Union


class Response(NamedTuple):
    content: Union[str, bytes]
    content_type: str
