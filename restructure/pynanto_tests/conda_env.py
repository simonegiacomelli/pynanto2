#!/usr/bin/env python3

from pathlib import Path


def name():
    return Path(__file__).parent.name


if __name__ == '__main__':
    print(name())
