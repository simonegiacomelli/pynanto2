import ast
import traceback

from js_pyi.produce import produce
from js_pyi.webidls import find, find_all


def test_correctness_0_quick():
    actual = produce([find('Document.webidl')])
    ast.parse(actual)


def test_correctness_1_all():
    exceptions = []
    for file in find_all():
        actual = produce([file])
        try:
            ast.parse(actual)
        except Exception as ex:
            exceptions.append((file, traceback.format_exc()))
    print()
    for file, ex in exceptions:
        print('=' * 50)
        print(file)
        print(ex)

    assert len(exceptions) == 0
