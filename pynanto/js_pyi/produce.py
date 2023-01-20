from __future__ import annotations

import ast
import traceback
from pathlib import Path
from typing import List

from js_pyi.ingest import ingest, merge, discard_unhandled, keep_unhandled
from js_pyi.stringify import s_statements
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

    python_code = s_statements(statements)

    return python_code


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
        print('-' * 50)
        print(ex)

    success = len(exceptions) == 0
    return success


def develop():
    for file in find_all():
        sts = ingest(file.read_text(), throw=False)
        sts = keep_unhandled(sts)
        if len(sts) > 0:
            python_code = s_statements(sts)
            print('=' * 50)
            print(file)
            print('-' * 50)
            print(python_code)
