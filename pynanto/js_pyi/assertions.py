from __future__ import annotations


def unhandled(argument):
    raise Exception(f'unhandled type={type(argument)} `{argument}`')


def expect_isinstance(instance, expected_type):
    if not isinstance(instance, expected_type):
        raise Exception(f' expect instance to be `{expected_type}` '
                        f'but instead found to be `{type(instance)}`')
