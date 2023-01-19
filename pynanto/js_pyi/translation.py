from __future__ import annotations

_types_dict = {
    'DOMString': 'str',
    'long': 'int',
    'long long': 'int',
    'unsigned long': 'int',
    'unsigned long long': 'int',
    'unsigned short': 'int',
}


def to_py_type(s) -> str:
    return _types_dict.get(s, s)


_values_dict = {
    'null': 'None',
}


def to_py_value(s) -> str:
    return _values_dict.get(s, s)
