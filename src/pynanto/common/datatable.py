from __future__ import annotations

from typing import Tuple, List


class Datatable:
    def __init__(self, rows: Tuple):
        assert len(rows) >= 1  # at least the header
        header = rows[0]
        assert all(map(lambda field_name: isinstance(field_name, str), header))  # verify header are strings
        self.rows: List[Row] = tuple(map(lambda r: Row(self, r), rows[1:]))
        self._field_index = {f.upper(): index for (index, f) in enumerate(header)}
        self.n = None
        super().__init__()

    def _valueByName(self, field_name: str, row: Row):
        index = self._field_index.get(field_name.upper(), None)
        if index is None:
            raise Exception(f'Field name not found `{field_name}`')
        return row[index]

    def __iter__(self):
        if self.n is not None:
            raise Exception('enumeration already started')
        self.n = 1
        return self

    def __next__(self):
        if self.n < len(self.rows):
            result = self.rows[self.n]
            self.n += 1
            return result
        else:
            self.n = None
            raise StopIteration


class Row(tuple):
    def __new__(cls, table: Datatable, iterable=...):
        instance = super().__new__(cls, iterable)
        instance._table = table
        return instance

    def valueByName(self, field_name: str):
        return self._table._valueByName(field_name, self)
