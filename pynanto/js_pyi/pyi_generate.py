from itertools import groupby
from pathlib import Path

from js_pyi.g_dataclasses import *
from js_pyi.ingest import ingest


def main():
    webidls_path = Path(__file__).parent / 'webidls'
    txt = ''
    for f in webidls_path.glob('enabled/Document.webidl'):
        print(f'file {f}')
        txt = f.read_text()
        break

    statements = ingest(txt, throw=False)
    interfaces = [s for s in statements if isinstance(s, GInterface)]

    int_by_name = dict({stmt_name: list(stmt_body) for (stmt_name, stmt_body) in groupby(interfaces, lambda i: i.name)})

    for stmt_name, stmt_body in int_by_name.items():
        print(f'class {stmt_name}')
        stmts: List[GStmt] = []
        e: GInterface
        for e in stmt_body:
            stmts.extend(e.body)
        for stmt in stmts:
            print(f'   ' + stmt.str())


if __name__ == '__main__':
    main()
