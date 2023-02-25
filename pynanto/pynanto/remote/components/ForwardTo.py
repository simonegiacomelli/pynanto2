def forward_to(host, guest_name: str):
    # def ga(self, attr):
    #     raise attr
    #
    #     def foo():
    #         return "foo"
    #
    #     return foo
    def ga(self, attr):
        guest_obj = getattr(self, guest_name)
        return getattr(guest_obj, attr)

    host.__getattr__ = ga
    return host


### tests

class Proxied:
    def __init__(self, string: str):
        self.string = string

    def foo(self):
        return self.string


class Target1:
    def __init__(self, guest):
        self.guest = guest

    def bar(self):
        return "bar"


def test_proxy():
    class Target2:
        def __init__(self, guest):
            self._guest = guest

    forward_to(Target1, 'guest')
    target1 = Target1(Proxied("foo"))
    assert target1.foo() == "foo"

    forward_to(Target2, '_guest')
    target2 = Target2(Proxied("bar"))
    assert target2.foo() == "bar"


def test_non_existant():
    forward_to(Target1, 'guest')
    target1 = Target1(Proxied("foo"))
    try:
        target1.does_not_exist()
        exception = None
    except Exception as ex:
        exception = ex

    assert exception is not None


def test_shouldNotForward_existingHostMethods():
    forward_to(Target1, 'guest')
    target1 = Target1(Proxied("foo"))
    assert "bar" == target1.bar()
