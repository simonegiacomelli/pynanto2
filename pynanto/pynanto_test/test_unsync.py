from pynanto.unsync import unsync


def test_unsync():
    @unsync
    async def fun():
        return 'ok'

    assert fun() == 'ok'


def test_unsync_with_args():
    @unsync
    async def fun(arg1):
        return arg1

    assert fun('foo') == 'foo'
