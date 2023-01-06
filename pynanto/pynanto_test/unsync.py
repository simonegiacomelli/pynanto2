import asyncio
import sys
import traceback
from threading import Thread


def unsync(f):
    result = None
    exc_info = None
    exception = None

    async def main_safe():
        nonlocal result, exc_info, exception
        try:
            result = await f()
        except Exception as ex:
            exception = ex
            exc_info = sys.exc_info()

    def start():
        asyncio.run(main_safe())

    def wrapper():
        nonlocal result, exc_info, exception
        thread = Thread(target=start)
        thread.start()
        thread.join()
        if exc_info is not None:
            exc_type, exc_value, exc_traceback = exc_info
            print('', file=sys.stderr)
            traceback.print_exception(exc_type, exc_value, exc_traceback, file=sys.stderr)
            raise exception
        return result

    return wrapper


def test_unsync():
    @unsync
    async def fun():
        return 'ok'

    assert fun() == 'ok'
