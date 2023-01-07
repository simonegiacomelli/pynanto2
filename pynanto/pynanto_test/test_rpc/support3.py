from typing import Dict


async def support3_mul(a: int, b: int) -> int:
    return a * b


async def support3_concat(a: str, b: str) -> str:
    return a + b


async def support3_with_typing_import() -> Dict[str, str]:
    return {'foo': 'bar'}
