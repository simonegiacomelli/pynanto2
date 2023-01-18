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
    todo(t)


def g_non_any_type(non_any_type: NonAnyType):
    expect_type(non_any_type, NonAnyType)

    t = non_any_type.type
    if isinstance(t, PrimitiveType):
        return g_primitive_type(t)
    elif isinstance(t, TypeIdentifier):
        return g_type_identifier(t)
    elif isinstance(t, Symbol):
        return g_symbol(t)
    todo(t)


def g_single_type(single_type: SingleType):
    expect_type(single_type, SingleType)
    t = single_type.type
    if isinstance(t, AnyType):
        todo(single_type)
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

    todo(t)


def g_argument(argument: Argument) -> str | GUnion:
    expect_type(argument, Argument)

    argument_type = argument.type
    if isinstance(argument_type, TypeWithExtendedAttributes):
        return g_type_with_extended_attributes(argument_type)

    return str(argument_type.type)


def c_InterfaceMember_method(member: InterfaceMember):
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
    else:
        todo(member.member)
    return GFunctionDef(member.name, GArguments(args=args), returns=returns)


def c_InterfaceMember_attribute(member: InterfaceMember):
    assert isinstance(member.member, Attribute)
    assert isinstance(member.member.attribute, AttributeRest)
    assert isinstance(member.member.attribute.type, TypeWithExtendedAttributes)
    return GAttribute(
        member.name,
        g_type_with_extended_attributes(member.member.attribute.type)
    )


def c_InterfaceMember(member: InterfaceMember):
    if member.idl_type == 'method':
        return c_InterfaceMember_method(member)
    if member.idl_type == 'attribute':
        return c_InterfaceMember_attribute(member)
    todo(member.idl_type)


def process_member(member: Construct):
    if isinstance(member, InterfaceMember):
        return c_InterfaceMember(member)
    elif isinstance(member, widlparser.ExtendedAttribute):
        return None
    else:
        todo(member)


def c_interface(c: Interface):
    members = remove_none(process_member(m) for m in c.members)
    return GClassDef(c.name, bases=interface_bases(c), body=members)


def g_construct(construct: Construct):
    expect_type(construct, Construct)

    if isinstance(construct, Interface):
        return c_interface(construct)

    todo(construct)


def g_union_type(union_type: UnionType):
    ann = [str(a) for a in union_type.types]
    g_union = GUnion(ann)
    return g_union


def generate(idl: str) -> List[GStmt]:
    statements: List[GStmt] = []
    parser = widlparser.Parser()
    parser.markup()
    parser.parse(idl)
    for c in parser.constructs:
        try:
            construct = g_construct(c)
        except Exception as ex:
            construct = GUnhandled(str(c), ex)
        statements.append(construct)
    return statements


def remove_none(param):
    return [m for m in param if m is not None]


def expect_type(instance, expected_type):
    if not isinstance(instance, expected_type):
        raise Exception(f' expect instance to be `{expected_type}` '
                        f'but instead found to be `{type(instance)}`')


def todo(argument):
    raise Exception(f'todo unhandled type={type(argument)} `{argument}`')
