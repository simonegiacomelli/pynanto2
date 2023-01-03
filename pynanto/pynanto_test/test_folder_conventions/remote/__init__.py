from common import common_mul  # absolute import are not handled if not in the root;

from js import document


async def main():
    document.body.innerHTML = f'remote=hello, common={common_mul(7, 6)}'
