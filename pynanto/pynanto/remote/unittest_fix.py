import os
import sys
import unittest
from pathlib import Path
from unittest import TestResult

from js import console


def unittest_main_fixed(module_name) -> TestResult:
    module = sys.modules[module_name]
    test_suit = unittest.TestLoader().loadTestsFromModule(module)

    return _test_runner_run(test_suit)


def run_all_tests() -> TestResult:
    script_dir = os.path.dirname(__file__)
    # async tests seems to not be supported
    # there are async tests in `common`
    # so only test suite from  `browser` package
    browser = (Path(script_dir) / '..').absolute()

    loader = unittest.TestLoader()
    test_suit = loader.discover(str(browser))
    return _test_runner_run(test_suit)


def _test_runner_run(test_suit) -> TestResult:
    txt = 'test_result.txt'
    with open(txt, 'w') as f:
        res = unittest.TextTestRunner(stream=f).run(test_suit)
    print(f'TextTestRunner: {res}')
    c = Path(txt).read_text()
    console.log(c)
    return res
