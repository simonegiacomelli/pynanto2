from __future__ import annotations

import widlparser
from widlparser import Interface, InterfaceMember, Construct, TypeWithExtendedAttributes, Argument, UnionType, \
    Attribute, AttributeRest, SingleType, AnyType, NonAnyType, PrimitiveType, Symbol, TypeIdentifier, Default

from js_pyi.g_dataclasses import *


class Processor:
    def __init__(self):
        self.module = GModule()

    def parse(self, idl: str):
        widl = widlparser.Parser()
        widl.markup()
        widl.parse(idl)
        for c in widl.constructs:
            self.module.append(self.g_construct(c))
        return self.module

    def c_interface(self, c: Interface):
        members = remove_none(self.process_member(m) for m in c.members)

        return GClassDef(c.name, bases=self.interface_bases(c), body=members)

    def c_InterfaceMember(self, member: InterfaceMember):
        if member.idl_type == 'method':
            return self.c_InterfaceMember_method(member)
        if member.idl_type == 'attribute':
            return self.c_InterfaceMember_attribute(member)
        todo(member.idl_type)

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
            expect_type(a, Argument)
            a: Argument
            annotation = self.g_argument(a)
            if not a.required:
                annotation = GOptional(annotation)
            g_arg = GArg(a.name, annotation)
            if a.default is not None:
                g_arg.default = self.g_default(a.default)
            args.append(g_arg)
        if isinstance(member.member, widlparser.Operation):
            returns = str(member.member.return_type).strip()
        else:
            todo(member.member)
        return GFunctionDef(member.name, GArguments(args=args), returns=returns)

    def process_member(self, member: Construct):
        if isinstance(member, InterfaceMember):
            return self.c_InterfaceMember(member)
        elif isinstance(member, widlparser.ExtendedAttribute):
            return None
        else:
            todo(member)

    def g_construct(self, construct: Construct):
        expect_type(construct, Construct)

        if isinstance(construct, Interface):
            return self.c_interface(construct)

        todo(construct)

    def g_argument(self, argument: Argument) -> str | GUnion:
        expect_type(argument, Argument)

        argument_type = argument.type
        if isinstance(argument_type, TypeWithExtendedAttributes):
            return self.g_type_with_extended_attributes(argument_type)

        return str(argument_type.type)

    def g_type_with_extended_attributes(self, twea: TypeWithExtendedAttributes):
        expect_type(twea, TypeWithExtendedAttributes)

        t = twea.type

        if isinstance(t, UnionType):
            return self.g_union_type(t)
        elif isinstance(t, SingleType):
            return self.g_single_type(t)

        todo(t)

    def g_union_type(self, union_type: UnionType):
        ann = [str(a) for a in union_type.types]
        # ann = ['None'] + ann
        g_union = GUnion(ann)
        return g_union

    def interface_bases(self, interface: Interface):
        if interface.inheritance is None:
            return []
        return [str(interface.inheritance.base)]

    def g_single_type(self, single_type: SingleType):
        expect_type(single_type, SingleType)
        t = single_type.type
        if isinstance(t, AnyType):
            todo(single_type)
        elif isinstance(t, NonAnyType):
            return self.g_non_any_type(t)

        return single_type.type_name

    def g_non_any_type(self, non_any_type: NonAnyType):
        expect_type(non_any_type, NonAnyType)

        t = non_any_type.type
        if isinstance(t, PrimitiveType):
            return self.g_primitive_type(t)
        elif isinstance(t, TypeIdentifier):
            return self.g_type_identifier(t)
        elif isinstance(t, Symbol):
            return self.g_symbol(t)
        todo(t)

    def g_primitive_type(self, primitive_type: PrimitiveType):
        expect_type(primitive_type, PrimitiveType)

        t = primitive_type.type
        if isinstance(t, Symbol):
            return self.g_symbol(t)
        todo(t)

    def g_type_identifier(self, ti: TypeIdentifier):
        expect_type(ti, TypeIdentifier)
        return ti.name

    def g_symbol(self, symbol: Symbol):
        expect_type(symbol, Symbol)
        s = symbol.symbol
        # if s == 'boolean':
        #     return 'bool'

        return s

    def g_default(self, default: Default):
        expect_type(default, Default)
        return default.value


def generate(idl: str) -> GModule:
    processor = Processor()
    processor.parse(idl)
    return processor.module


def remove_none(param):
    return [m for m in param if m is not None]


def expect_type(instance, expected_type):
    if not isinstance(instance, expected_type):
        raise Exception(f' expect instance to be `{expected_type}` '
                        f'but instead found to be `{type(instance)}`')


def todo(argument):
    raise Exception(f'todo unhandled type={type(argument)} `{argument}`')
