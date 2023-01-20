from __future__ import annotations

import ast
import traceback
from io import StringIO
from pathlib import Path
from typing import List

from js_pyi.ingest import ingest, merge, discard_unhandled
from js_pyi.webidls import find_all


def produce(files: List[Path] | None = None) -> str:
    if files is None:
        files = find_all()

    statements = []
    for file in files:
        sts = ingest(file.read_text(), throw=False)
        sts = discard_unhandled(sts)
        statements.extend(sts)

    statements = merge(statements)

    res = StringIO()
    for st in statements:
        res.write(st.to_python() + '\n')

    return res.getvalue()


def parse_product() -> bool:
    exceptions = []
    for file in find_all():
        actual = produce([file])
        try:
            ast.parse(actual)
        except Exception as ex:
            exceptions.append((file, traceback.format_exc()))
    print()
    for file, ex in exceptions:
        print('=' * 50)
        print(file)
        print(ex)

    success = len(exceptions) == 0
    return success
