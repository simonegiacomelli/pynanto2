from pynanto.common.datatable import Datatable


def test_fieldValue():
    target = Datatable((('field1',), ('one',)))
    assert 'one' == target.rows[0].valueByName('field1')


def test_fieldByName():
    target = Datatable((('field1',), ('one',)))
    assert 'one' == target.rows[0].fieldByName('field1').asString
