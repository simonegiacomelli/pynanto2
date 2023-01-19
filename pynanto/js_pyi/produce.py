from __future__ import annotations

from io import StringIO
from pathlib import Path
from typing import List

from js_pyi.ingest import ingest, merge, discard_unhandled_inplace
from js_pyi.webidls import find_all


def produce(files: List[Path] | None = None) -> str:
    if files is None:
        files = find_all()

    statements = []
    for file in files:
        statements.extend(ingest(file.read_text(), throw=False))

    statements = merge(statements)

    discard_unhandled_inplace(statements)
    res = StringIO()
    for st in statements:
        res.write(st.to_python() + '\n')

    return res.getvalue()
