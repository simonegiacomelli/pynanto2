from __future__ import annotations

import widlparser
from widlparser import Interface, InterfaceMember, Construct, TypeWithExtendedAttributes, Argument, UnionType

from js_pyi.g_dataclasses import *


class Processor:
    def __init__(self):
        self.module = GModule()

    def parse(self, idl: str):
        widl = widlparser.Parser()
        widl.markup()
        widl.parse(idl)
        for c in widl.constructs:
            self.module.append(self.process(c))
        return self.module

    def c_interface(self, c: Interface):
        members = remove_none(self.process_member(m) for m in c.members)

        return GClassDef(c.name, bases=self.interface_bases(c), body=members)

    def c_InterfaceMember(self, member: InterfaceMember):
        args = []
        for a in member.arguments:
            args.append(
                GArg(a.name, self.g_arg_annotation(a))
            )
        if isinstance(member.member, widlparser.Operation):
            returns = str(member.member.return_type).strip()
        else:
            raise Exception('todo')
        return GFunctionDef(member.name, GArguments(args=args), returns=returns)

    def process_member(self, member: Construct):
        if isinstance(member, InterfaceMember):
            return self.c_InterfaceMember(member)
        elif isinstance(member, widlparser.ExtendedAttribute):
            return None
        else:
            raise Exception(f'todo `{type(member)}` `{str(member)}`')

    def process(self, construct: Construct):
        if isinstance(construct, Interface):
            return self.c_interface(construct)
        else:
            return None

    def g_arg_annotation(self, argument: Argument) -> str | GUnion:
        argument_type = argument.type
        if isinstance(argument_type, TypeWithExtendedAttributes):
            if isinstance(argument_type.type, UnionType):
                ut: UnionType = argument_type.type
                ann = [str(a) for a in ut.types]
                ann = ['None'] + ann
                return GUnion(ann)
            else:
                raise Exception('todo')

        return str(argument_type.type)

    def interface_bases(self, interface: Interface):
        if interface.inheritance is None:
            return []
        return [str(interface.inheritance.base)]


def generate(idl: str) -> GModule:
    processor = Processor()
    processor.parse(idl)
    return processor.module


def remove_none(param):
    return [m for m in param if m is not None]
