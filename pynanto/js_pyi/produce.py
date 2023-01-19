from itertools import groupby
from pathlib import Path
from typing import List

from js_pyi.datamodel import GInterface, GStmt, GUnhandled
from js_pyi.ingest import ingest
from js_pyi.tee import Tee


def produce(webidl: Path) -> str:
    txt = webidl.read_text()

    statements = ingest(txt, throw=False)
    # for s in statements:
    #     print(s)
    interfaces = [s for s in statements if isinstance(s, GInterface)]

    int_by_name = dict({stmt_name: list(stmt_body) for (stmt_name, stmt_body) in groupby(interfaces, lambda i: i.name)})

    tee = Tee(output=None)

    for stmt_name, stmt_body in int_by_name.items():
        tee.appendln(f'class {stmt_name}')
        stmts: List[GStmt] = []
        e: GInterface
        for e in stmt_body:
            stmts.extend(e.body)
        for stmt in stmts:
            if isinstance(stmt, GUnhandled):
                continue
            tee.appendln(f'   ' + stmt.str())

    return str(tee)
