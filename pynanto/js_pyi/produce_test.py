import ast

from js_pyi.produce import produce, parse_product
from js_pyi.webidls import find


def test_correctness_0_quick():
    actual = produce([find('Document.webidl')])
    ast.parse(actual)


def test_correctness_1_all():
    success = parse_product()
    assert success
