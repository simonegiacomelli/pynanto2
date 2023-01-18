from __future__ import annotations

import widlparser
from widlparser import Interface, InterfaceMember, Construct, TypeWithExtendedAttributes, Argument, UnionType, \
    Attribute, AttributeRest, SingleType, AnyType, NonAnyType, PrimitiveType, Symbol, TypeIdentifier, Default

from js_pyi.g_dataclasses import *


def g_symbol(symbol: Symbol):
    expect_type(symbol, Symbol)
    s = symbol.symbol

    return s


def g_default(default: Default):
    expect_type(default, Default)
    return default.value


def g_type_identifier(ti: TypeIdentifier):
    expect_type(ti, TypeIdentifier)
    return ti.name


def g_primitive_type(primitive_type: PrimitiveType):
    expect_type(primitive_type, PrimitiveType)

    t = primitive_type.type
    if isinstance(t, Symbol):
        return g_symbol(t)
    unhandled(t)


def g_non_any_type(non_any_type: NonAnyType):
    expect_type(non_any_type, NonAnyType)

    t = non_any_type.type
    if isinstance(t, PrimitiveType):
        return g_primitive_type(t)
    elif isinstance(t, TypeIdentifier):
        return g_type_identifier(t)
    elif isinstance(t, Symbol):
        return g_symbol(t)
    unhandled(t)


def g_single_type(single_type: SingleType):
    expect_type(single_type, SingleType)
    t = single_type.type
    if isinstance(t, AnyType):
        unhandled(single_type)
    elif isinstance(t, NonAnyType):
        return g_non_any_type(t)

    return single_type.type_name


def interface_bases(interface: Interface):
    if interface.inheritance is None:
        return []
    return [str(interface.inheritance.base)]


def g_type_with_extended_attributes(twea: TypeWithExtendedAttributes):
    expect_type(twea, TypeWithExtendedAttributes)

    t = twea.type

    if isinstance(t, UnionType):
        return g_union_type(t)
    elif isinstance(t, SingleType):
        return g_single_type(t)

    unhandled(t)


def g_argument(argument: Argument) -> str | GUnion:
    expect_type(argument, Argument)

    argument_type = argument.type
    if isinstance(argument_type, TypeWithExtendedAttributes):
        return g_type_with_extended_attributes(argument_type)

    return str(argument_type.type)


def c_interface_member__type_method(member: InterfaceMember):
    expect_type(member, InterfaceMember)

    args = []
    for a in member.arguments:
        expect_type(a, Argument)
        a: Argument
        annotation = g_argument(a)
        if not a.required:
            annotation = GOptional(annotation)
        g_arg = GArg(a.name, annotation)
        if a.default is not None:
            g_arg.default = g_default(a.default)
        args.append(g_arg)

    if isinstance(member.member, widlparser.Operation):
        returns = str(member.member.return_type).strip()
        return GMethod(member.name, GArguments(args=args), returns=returns)

    unhandled(member.member)


def c_interface_member__type_attribute(im: InterfaceMember):
    expect_type(im, InterfaceMember)
    expect_type(im.member, Attribute)

    attribute: Attribute = im.member

    expect_type(attribute.attribute, AttributeRest)
    expect_type(attribute.attribute.type, TypeWithExtendedAttributes)
    return GAttribute(
        im.name,
        g_type_with_extended_attributes(attribute.attribute.type)
    )


def g_interface_member(member: InterfaceMember):
    expect_type(member, InterfaceMember)

    idl_type = member.idl_type

    if idl_type == 'method':
        return c_interface_member__type_method(member)
    if idl_type == 'attribute':
        return c_interface_member__type_attribute(member)

    unhandled(idl_type)


def g_interface(interface: Interface):
    expect_type(interface, Interface)
    members = [g_construct(construct) for construct in interface.members]
    return GInterface(interface.name, bases=interface_bases(interface), body=members)


def g_construct(construct: Construct):
    expect_type(construct, Construct)

    if isinstance(construct, Interface):
        return g_interface(construct)
    if isinstance(construct, InterfaceMember):
        return g_interface_member(construct)

    unhandled(construct)


def g_union_type(union_type: UnionType):
    ann = [str(a) for a in union_type.types]
    g_union = GUnion(ann)
    return g_union


def generate(idl: str, throw: bool = True) -> List[GStmt]:
    statements: List[GStmt] = []
    parser = widlparser.Parser()
    parser.markup()
    parser.parse(idl)
    for c in parser.constructs:
        if throw:
            construct = g_construct(c)
        else:
            try:
                construct = g_construct(c)
            except Exception as ex:
                construct = GUnhandled(str(c), ex)
        statements.append(construct)
    return statements


def expect_type(instance, expected_type):
    if not isinstance(instance, expected_type):
        raise Exception(f' expect instance to be `{expected_type}` '
                        f'but instead found to be `{type(instance)}`')


def unhandled(argument):
    raise Exception(f'todo unhandled type={type(argument)} `{argument}`')
