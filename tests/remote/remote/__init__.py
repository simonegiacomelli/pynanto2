from pathlib import Path


# tw.main()


async def main():
    from .tree import print_tree
    path = Path(__file__)
    print(path)
    print_tree('/default_bundle')
    from js import pyodide
    await pyodide.loadPackage('pytest')
    import pytest
    pytest.main(['/default_bundle/remote'])
    pass
