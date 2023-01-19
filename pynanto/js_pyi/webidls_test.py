from js_pyi.webidls import find


def test_webidls_presence():
    assert 'interface Document' in find('Document.webidl').read_text()
    assert 'interface Bluetooth' in find('Bluetooth.webidl').read_text()
    assert 'interface PaymentRequest' in find('PaymentRequest.webidl').read_text()
