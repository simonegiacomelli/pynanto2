import inspect
import json


def divide(a: int, b: int) -> float:
    return a / b


def test_intro1():
    i = inspect.signature(divide)
    s = json.dumps(i)
    print(s)
