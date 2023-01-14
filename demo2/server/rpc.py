from pathlib import Path


async def read_file_unsecure(filename: str):
    return Path(filename).read_text()
