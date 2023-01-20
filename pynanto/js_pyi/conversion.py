from __future__ import annotations

_types_dict = {
    'undefined': 'None',
    'DOMString': 'str',
    'long': 'int',
    'long long': 'int',
    'unsigned long': 'int',
    'unsigned long long': 'int',
    'unsigned short': 'int',
    'boolean': 'bool',
    'double': 'float',
    'unrestricted double': 'float',
    'unrestricted float': 'float',
    # generics
    'sequence': 'Sequence',
    'Promise': 'Awaitable'
}


def to_py_type(s) -> str:
    return _types_dict.get(s, s)


_values_dict = {
    'null': 'None',
}


def to_py_value(s) -> str:
    return _values_dict.get(s, s)


_names_dict = {
    'async': 'async_',
}


def to_py_name(s) -> str:
    return _names_dict.get(s, s)
