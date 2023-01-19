from __future__ import annotations

from io import StringIO
from pathlib import Path

from js_pyi.ingest import ingest, merge, discard_unhandled_inplace


def produce(webidl: Path) -> str:
    txt = webidl.read_text()

    statements = merge(ingest(txt, throw=False))

    discard_unhandled_inplace(statements)
    res = StringIO()
    for st in statements:
        res.write(st.to_python() + '\n')

    return res.getvalue()
