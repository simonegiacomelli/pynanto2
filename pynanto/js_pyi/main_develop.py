from __future__ import annotations

from pathlib import Path
from typing import List

from js_pyi.datamodel import GStmt, GClass
from js_pyi.ingest import ingest
from js_pyi.stringify import s_statements
from js_pyi.webidls import find_all


def _keep_classes_with_overloads(sts: List[GStmt]) -> List[GStmt]:
    result = []
    for st in sts:
        if not isinstance(st, GClass):
            continue


def develop(files: List[Path] | None = None):
    if files is None:
        files = find_all()

    for file in files:
        sts = ingest(file.read_text(), throw=False)
        sts = _keep_classes_with_overloads(sts)
        if len(sts) > 0:
            python_code = s_statements(sts)
            print('=' * 50)
            print(file)
            print('-' * 50)
            print(python_code)


def main():
    develop()


if __name__ == '__main__':
    main()
