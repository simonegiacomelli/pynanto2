import io
from contextlib import suppress
from itertools import groupby
from pathlib import Path

import widlparser
from widlparser import Construct, Interface, InterfaceMember


class Processor:
    def __init__(self):
        self.out = io.StringIO()

    def c_interface(self, c: Interface):
        o = self.out
        o.write(f'class {c.name}:\n')

        for m in c.members:
            self.process_member(m)

    def c_InterfaceMember(self, member: InterfaceMember):
        o = self.out
        t = ''
        with suppress(Exception):
            attribute_type = member.member.attribute.type
            t = (': ' + str(attribute_type)).strip()
            if t.endswith('?'):
                t = t.replace('?', '') + ' | None'
            else:
                pass
            if t.startswith('DOMString'):
                t.replace('DOMString', 'str')
            if t.startswith('boolean'):
                t.replace('boolean', 'bool')
        name = member.name
        if name == 'getElementsByTagName':
            pass
        else:
            pass
        o.write(f'    {name}{t}')

        o.write('\n')

    def process_member(self, member: Construct):
        if isinstance(member, InterfaceMember):
            self.c_InterfaceMember(member)

    def process(self, construct: Construct):
        if isinstance(construct, Interface):
            self.c_interface(construct)


def associateby(iterable, key_selector):
    return {k: next(v) for k, v in groupby(iterable, key_selector)}


def main():
    widl = widlparser.Parser()

    webidls_path = Path(__file__).parent / 'webidls'
    for f in webidls_path.glob('enabled/Document.webidl'):
        print(f'file {f}')
        txt = f.read_text()
        widl.parse(txt)
    processor = Processor()
    g = groupby(widl.constructs, lambda c: c.name)
    constructs_by_name = {k: list(v) for k, v in g}
    for c in widl.constructs:
        processor.process(c)

    print(processor.out.getvalue())


if __name__ == '__main__':
    main()
