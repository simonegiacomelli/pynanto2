from __future__ import annotations

import widlparser
from widlparser import Interface, InterfaceMember, Construct, TypeWithExtendedAttributes, Argument, UnionType, \
    Attribute, AttributeRest, SingleType

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
        if member.idl_type == 'method':
            return self.c_InterfaceMember_method(member)
        if member.idl_type == 'attribute':
            return self.c_InterfaceMember_attribute(member)
        raise Exception(f'todo {member.idl_type}')

    def c_InterfaceMember_attribute(self, member: InterfaceMember):
        assert isinstance(member.member, Attribute)
        assert isinstance(member.member.attribute, AttributeRest)
        assert isinstance(member.member.attribute.type, TypeWithExtendedAttributes)
        return GAttribute(
            member.name,
            self.g_type_with_extended_attributes(member.member.attribute.type)
        )

    def c_InterfaceMember_method(self, member: InterfaceMember):

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
                return self.g_type_with_extended_attributes(argument_type)
            else:
                raise Exception('todo')

        return str(argument_type.type)

    def g_type_with_extended_attributes(self, argument_type: TypeWithExtendedAttributes):
        if isinstance(argument_type.type, UnionType):
            ut: UnionType = argument_type.type
            ann = [str(a) for a in ut.types]
            ann = ['None'] + ann
            g_union = GUnion(ann)
            return g_union
        elif isinstance(argument_type.type, SingleType):
            sg: SingleType = argument_type.type
            return sg.type_name
        else:
            raise Exception(f'todo {argument_type.type}')

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
