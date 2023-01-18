from __future__ import annotations

import widlparser
from widlparser import Interface, InterfaceMember, Construct, TypeWithExtendedAttributes, Argument, UnionType, \
    Attribute, AttributeRest, SingleType, AnyType, NonAnyType, PrimitiveType, Symbol, TypeIdentifier, Default, Type

from js_pyi.g_dataclasses import *


def i_symbol(symbol: Symbol):
    _expect_type(symbol, Symbol)
    s = symbol.symbol

    return s


def i_default(default: Default):
    _expect_type(default, Default)
    return default.value


def i_type_identifier(ti: TypeIdentifier):
    _expect_type(ti, TypeIdentifier)
    return ti.name


def i_primitive_type(primitive_type: PrimitiveType):
    _expect_type(primitive_type, PrimitiveType)

    t = primitive_type.type
    if isinstance(t, Symbol):
        return i_symbol(t)
    _unhandled(t)


def i_non_any_type(non_any_type: NonAnyType):
    _expect_type(non_any_type, NonAnyType)

    t = non_any_type.type
    if isinstance(t, PrimitiveType):
        return i_primitive_type(t)
    elif isinstance(t, TypeIdentifier):
        return i_type_identifier(t)
    elif isinstance(t, Symbol):
        return i_symbol(t)
    _unhandled(t)


def i_single_type(single_type: SingleType):
    _expect_type(single_type, SingleType)
    t = single_type.type
    if isinstance(t, AnyType):
        _unhandled(single_type)
    elif isinstance(t, NonAnyType):
        return i_non_any_type(t)

    return single_type.type_name


def interface_bases(interface: Interface):
    if interface.inheritance is None:
        return []
    return [str(interface.inheritance.base)]


def i_type_with_extended_attributes(twea: TypeWithExtendedAttributes):
    _expect_type(twea, TypeWithExtendedAttributes)

    t = twea.type

    if isinstance(t, UnionType):
        return i_union_type(t)
    elif isinstance(t, SingleType):
        return i_single_type(t)

    _unhandled(t)


def i_type(t: Type):
    _expect_type(t, Type)

    tt = t.type
    if isinstance(tt, SingleType):
        return i_single_type(tt)
    _unhandled(t)


def i_argument(argument: Argument):
    _expect_type(argument, Argument)

    argument_type = argument.type
    if isinstance(argument_type, Type):
        return i_type(argument_type)
    elif isinstance(argument_type, TypeWithExtendedAttributes):
        return i_type_with_extended_attributes(argument_type)

    return str(argument_type.type)


def i_interface_member__type_method(member: InterfaceMember):
    _expect_type(member, InterfaceMember)

    args = []
    for a in member.arguments:
        _expect_type(a, Argument)
        a: Argument
        annotation = i_argument(a)
        if not a.required:
            annotation = GNotRequired(annotation)
        g_arg = GArg(a.name, annotation)
        if a.default is not None:
            g_arg.default = i_default(a.default)
        args.append(g_arg)

    if isinstance(member.member, widlparser.Operation):
        returns = str(member.member.return_type).strip()
        return GMethod(member.name, arguments=args, returns=returns)

    _unhandled(member.member)


def i_interface_member__type_attribute(im: InterfaceMember):
    _expect_type(im, InterfaceMember)
    _expect_type(im.member, Attribute)

    attribute: Attribute = im.member

    _expect_type(attribute.attribute, AttributeRest)
    _expect_type(attribute.attribute.type, TypeWithExtendedAttributes)
    return GAttribute(
        im.name,
        i_type_with_extended_attributes(attribute.attribute.type)
    )


def i_interface_member(member: InterfaceMember):
    _expect_type(member, InterfaceMember)

    idl_type = member.idl_type

    if idl_type == 'method':
        return i_interface_member__type_method(member)
    if idl_type == 'attribute':
        return i_interface_member__type_attribute(member)

    _unhandled(idl_type)


def i_interface(interface: Interface):
    _expect_type(interface, Interface)
    members = [i_construct(construct) for construct in interface.members]
    return GInterface(interface.name, bases=interface_bases(interface), body=members)


def i_construct(construct: Construct):
    _expect_type(construct, Construct)

    if isinstance(construct, Interface):
        return i_interface(construct)
    if isinstance(construct, InterfaceMember):
        return i_interface_member(construct)

    _unhandled(construct)


def i_union_type(union_type: UnionType):
    ann = [str(a) for a in union_type.types]
    g_union = GUnion(ann)
    return g_union


def ingest(idl: str, throw: bool = True) -> List[GStmt]:
    statements: List[GStmt] = []
    parser = widlparser.Parser()
    parser.markup()
    parser.parse(idl)
    for c in parser.constructs:
        if throw:
            construct = i_construct(c)
        else:
            try:
                construct = i_construct(c)
            except Exception as ex:
                construct = GUnhandled(str(c), ex)
        statements.append(construct)
    return statements


def _expect_type(instance, expected_type):
    if not isinstance(instance, expected_type):
        raise Exception(f' expect instance to be `{expected_type}` '
                        f'but instead found to be `{type(instance)}`')


def _unhandled(argument):
    raise Exception(f'todo unhandled type={type(argument)} `{argument}`')
