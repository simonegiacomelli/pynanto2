from pynanto.common.datatable import Datatable


def test_fieldValue():
    target = new_target()
    assert 'one' == target.rows[0].valueByName('field1')


def test_fieldByName():
    target = new_target()
    assert 'one' == target.rows[0].fieldByName('field1').value
    assert 'field1' == target.rows[0].fieldByName('field1').name.lower()


def test_write():
    target = new_target()
    target.rows[0].fieldByName('field1').value = 'mod1'
    assert 'mod1' == target.rows[0].fieldByName('field1').value


def mock_rows():
    return ('field1',), ('one',)


def new_target():
    return Datatable(mock_rows())
