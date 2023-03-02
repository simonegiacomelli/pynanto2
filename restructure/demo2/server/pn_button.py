class Prox:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'


class PnButton:

    def __init__(self):
        _proxy = Prox()
        _proxy.innerHTML = 'button'
        self._proxy = _proxy
        # setattr(self, '_proxy', _proxy)
        # document.body.append(self._proxy)

    def __getattr__(self, attr):
        if attr == '_proxy':
            return self._proxy
        return getattr(self._proxy, attr)

    def __setattr__(self, key, value):
        if key == '_proxy':
            super().__setattr__(key, value)
        else:
            setattr(self._proxy, key, value)


def main():
    btn = PnButton()
    b = btn.b
    btn.a = b
    print(f'btn.a = {btn.a}')
    assert btn.a == 'b'


if __name__ == '__main__':
    main()
