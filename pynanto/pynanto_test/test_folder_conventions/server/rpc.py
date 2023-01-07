# the module only_server will not be transferred to the remote
# so if it works, it means the invocation ended up actually
# on the server side
from .only_server import constant


async def server_information() -> str:
    return str(constant())
