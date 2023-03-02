import inspect
import os
import unittest
from inspect import getsourcefile
from os.path import abspath
from pathlib import Path


def run():
    print(f'cwd={os.getcwd()}')
    print(f'__name__={__name__}\n__file__={__file__}\n__package__={__package__}')
    print(f'absolute={Path(__file__).resolve()}')
    s1 = abspath(getsourcefile(lambda: 0))
    print(f'getsourcefile={s1}')
    s2 = inspect.getframeinfo(inspect.currentframe()).filename
    print(f'getframeinfo(inspect.currentframe()).filename={s2}')
    return s2


prev = run()
os.chdir(Path(__file__).parent)

post = run()

unittest.TestCase().assertEqual(prev, post)
