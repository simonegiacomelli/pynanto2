import datetime
import platform
from functools import partial


def clip_copy(data: str):
    s = platform.system()
    if s == 'Linux':
        fun = partial(_process, 'xclip -sel c', data)
    elif s == 'Darwin':
        fun = partial(_process, 'pbcopy', data)
    else:
        raise Exception(f'System platform not supported {s}')
    fun()


def _process(cmd: str, data: str):
    import shlex
    args = shlex.split(cmd)
    from subprocess import Popen, PIPE, STDOUT
    p = Popen(args, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    p.stdin.write(data.encode())


if __name__ == '__main__':
    clip_copy(f'ciao {datetime.datetime.now()}')
