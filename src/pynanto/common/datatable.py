from __future__ import annotations

from typing import Tuple, List


class Datatable:
    def __init__(self, rows: Tuple):
        assert len(rows) >= 1  # at least the header
        header = rows[0]
        assert all(map(lambda field_name: isinstance(field_name, str), header))  # verify header are strings
        self.rows: List[Row] = list(map(lambda r: Row(self, r), rows[1:]))
        self._field_index_dict = {f.upper(): index for (index, f) in enumerate(header)}
        self._n = None
        super().__init__()

    def _fieldByName(self, field_name: str, row: Row) -> Field:
        field_name = field_name.upper()
        value = self._valueByName(field_name, row)
        return Field(field_name, value, row, self)

    def _valueByName(self, field_name: str, row: Row):
        index = self._field_index(field_name)
        return row[index]

    def _field_index(self, field_name):
        index = self._field_index_dict.get(field_name.upper(), None)
        if index is None:
            raise Exception(f'Field name not found `{field_name}`')
        return index

    def __iter__(self):
        if self._n is not None:
            raise Exception('enumeration already started')
        self._n = 1
        return self

    def __next__(self):
        if self._n < len(self.rows):
            result = self.rows[self._n]
            self._n += 1
            return result
        else:
            self._n = None
            raise StopIteration

    def _set_value(self, field_name: str, row: Row, value: any):
        index = self._field_index(field_name)
        row[index] = value


class Field:
    def __init__(self, name: str, value, row: Row, table: Datatable):
        self.name = name
        self._row = row
        self._value = value
        self._table = table

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._table._set_value(self.name, self._row, value)


class Row(list):

    def __init__(self, table: Datatable, iterable=...):
        super().__init__(iterable)
        self._table = table

    def valueByName(self, field_name: str):
        return self._table._valueByName(field_name, self)

    def fieldByName(self, field_name: str) -> Field:
        return self._table._fieldByName(field_name, self)
