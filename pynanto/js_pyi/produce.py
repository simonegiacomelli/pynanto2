from pathlib import Path

from js_pyi.ingest import ingest, merge, discard_unhandled_inplace
from js_pyi.tee import Tee


def produce(webidl: Path) -> str:
    txt = webidl.read_text()

    statements = merge(ingest(txt, throw=False))

    discard_unhandled_inplace(statements)

    tee = Tee(output=None)

    for st in statements:
        tee.appendln(st.to_python())

    return str(tee)
