from itertools import groupby
from pathlib import Path

from js_pyi.clipboard import clip_copy
from js_pyi.datamodel import *
from js_pyi.ingest import ingest
from js_pyi.tee import Tee


def main():
    webidls_path = Path(__file__).parent / 'webidls'
    txt = ''
    for f in webidls_path.glob('enabled/Document.webidl'):
        print(f'file {f}')
        txt = f.read_text()
        break

    statements = ingest(txt, throw=False)
    for s in statements:
        print(s)
    interfaces = [s for s in statements if isinstance(s, GInterface)]

    int_by_name = dict({stmt_name: list(stmt_body) for (stmt_name, stmt_body) in groupby(interfaces, lambda i: i.name)})

    tee = Tee()

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

    clip_copy(str(tee))


if __name__ == '__main__':
    main()
