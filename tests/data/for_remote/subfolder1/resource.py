from pathlib import Path

parent = Path(__file__).parent


def content() -> str:
    return (parent / 'resource.txt').read_text()
