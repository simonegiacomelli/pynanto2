from __future__ import annotations

import itertools
from typing import Dict


def groupby(iterable, key) -> Dict:
    return {k: list(v) for (k, v) in itertools.groupby(iterable, key)}


def partition(iterable, key):
    sx = []
    dx = []
    for item in iterable:
        if key(item):
            sx.append(item)
        else:
            dx.append(item)
    return sx, dx


def remove_inplace(array, key):
    for idx in reversed(range(len(array))):
        st = array[idx]
        if key(st):
            del array[idx]
