import ast

from js_pyi.produce import produce
from js_pyi.webidls import find


def test_output_correctness():
    actual = produce(find('Document.webidl'))
    ast.parse(actual)
