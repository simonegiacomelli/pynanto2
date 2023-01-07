from common import common_mul  # absolute import are not handled if not in the root;

from js import document
from pynanto_test.test_folder_conventions.server.rpc import server_information


async def main():
    com = common_mul(7, 6)
    ser = await server_information()
    document.body.innerHTML = f'remote=hello, common={com}, server={ser}'
