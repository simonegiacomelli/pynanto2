from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from js_pyi.g_dataclasses import *


def g_attribute(a: GAttribute) -> str:
    return a.name + ': ' + a.annotation


def g_method(m: GMethod) -> str:
    return f'def {m.name}(): ...'
