######################## start - remote test execution ###################
import re
from pathlib import Path
from typing import Union

import pytest
from _pytest._code import ExceptionInfo
from _pytest._code.code import TerminalRepr
from py._path.local import LocalPath


def pytest_sessionstart(session):
    pluginmanager = session.config.pluginmanager

    if not session.config.option.collectonly:
        pluginmanager.unregister(name='python')

    # capmanager = pluginmanager.getplugin('capturemanager')
    # capmanager.suspend_global_capture(in_=True)
    # capmanager.resume_global_capture()


def pytest_addoption(parser):
    pass


accepted_root = Path(__file__).parent
self_file = Path(__file__)


def pytest_collect_file(file_path: Path, path: LocalPath, parent):
    # if self_file == file_path:
    #     return StbtCollector.from_parent(parent, path=file_path.parent)
    # else:
    #     None
    parents = list(file_path.parents)
    if path.ext == ".py" and accepted_root in parents:
        return StbtCollector.from_parent(parent, path=file_path)
    else:
        return None


class StbtCollector(pytest.File):
    def collect(self):
        # yield StbtRemoteTest.from_parent(self, filename='supermock.py', testname='fake_test', line_number=42)
        with open(self.fspath.strpath) as f:
            # We implement our own parsing to avoid import stbt ImportErrors
            for n, line in enumerate(f):
                m = re.match(r'^def\s+(test_[a-zA-Z0-9_]*)', line)
                if m:
                    yield StbtRemoteTest.from_parent(self, filename=self.fspath, testname=m.group(1), line_number=n + 1)


class StbtRemoteTest(pytest.Item):
    def __init__(self, parent, filename, testname, line_number):
        print(f'StbtRemoteTest {parent} {filename} {testname}')
        super(StbtRemoteTest, self).__init__(testname, parent)
        self._filename = filename
        self._testname = testname
        self._line_number = line_number

    def __repr__(self):
        return "StbtRemoteTest(%r, %r, %r)" % (self._filename, self._testname, self._line_number)

    def runtest(self):
        if 'will_fail' in self._testname:
            raise Exception('Synthetic exception!')

    def reportinfo(self):
        return self.fspath, self._line_number, ""

    def repr_failure(self, excinfo: ExceptionInfo[BaseException],
                     style: 'Optional[_TracebackStyle]' = None) -> Union[str, TerminalRepr]:
        return 'failed'
        traceback = excinfo.traceback
        ntraceback = traceback.cut(path=__file__)
        excinfo.traceback = ntraceback.filter()

        return excinfo.getrepr(funcargs=True,
                               showlocals=False,
                               style="short", tbfilter=False)

######################## end   - remote test execution ###################
