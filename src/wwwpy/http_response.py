from typing import NamedTuple, Union


class HttpResponse(NamedTuple):
    content: Union[str, bytes]
    content_type: str

    @staticmethod
    def application_zip(content: bytes):
        content_type = 'application/zip, application/octet-stream, application/x-zip-compressed, multipart/x-zip'
        return HttpResponse(content, content_type)
