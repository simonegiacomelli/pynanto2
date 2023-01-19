from __future__ import annotations

from itertools import groupby

import widlparser
from widlparser import Interface, InterfaceMember, Construct, TypeWithExtendedAttributes, Argument, UnionType, \
    Attribute, AttributeRest, SingleType, AnyType, NonAnyType, PrimitiveType, Symbol, TypeIdentifier, Default, Type, \
    TypeSuffix, Operation, UnionMemberType, UnsignedIntegerType

from js_pyi.datamodel import *
from js_pyi.datamodel import unhandled, expect_type
from js_pyi.itertools import groupby, partition, remove_inplace

_none = 'None'


def i_symbol(symbol: Symbol):
    expect_type(symbol, Symbol)
    s = symbol.symbol

    return s


def i_default(default: Default):
    expect_type(default, Default)
    return default.value


def i_type_identifier(ti: TypeIdentifier):
    expect_type(ti, TypeIdentifier)
    return ti.name


def i_primitive_type(primitive_type: PrimitiveType):
    expect_type(primitive_type, PrimitiveType)

    t = primitive_type.type
    if isinstance(t, Symbol):
        return i_symbol(t)
    if isinstance(t, UnsignedIntegerType):
        s = str(t)
        return s
    unhandled(t)


def i_non_any_type(non_any_type: NonAnyType):
    expect_type(non_any_type, NonAnyType)

    res = None
    t = non_any_type.type
    if isinstance(t, PrimitiveType):
        res = i_primitive_type(t)
    elif isinstance(t, TypeIdentifier):
        res = i_type_identifier(t)
    elif isinstance(t, Symbol):
        res = i_symbol(t)
    elif isinstance(t, TypeWithExtendedAttributes):
        # generics
        unhandled(t)
        # res = i_type_with_extended_attributes(t)
    else:
        unhandled(t)

    res = _wrap_if_nullable(res, non_any_type.suffix)

    return res


def i_single_type(single_type: SingleType):
    expect_type(single_type, SingleType)
    t = single_type.type
    if isinstance(t, AnyType):
        unhandled(single_type)
    elif isinstance(t, NonAnyType):
        return i_non_any_type(t)

    return single_type.type_name


def interface_bases(interface: Interface):
    if interface.inheritance is None:
        return []
    return [str(interface.inheritance.base)]


def i_type_with_extended_attributes(twea: TypeWithExtendedAttributes):
    expect_type(twea, TypeWithExtendedAttributes)

    t = twea.type
    if isinstance(t, UnionType):
        res = i_union_type(t)
    elif isinstance(t, SingleType):
        res = i_single_type(t)
    else:
        unhandled(t)

    return _wrap_if_nullable(res, twea.suffix)


def i_type(t: Type):
    expect_type(t, Type)

    tt = t.type
    if isinstance(tt, SingleType):
        res = i_single_type(tt)
    elif isinstance(tt, UnionType):
        res = i_union_type(tt)
    else:
        unhandled(tt)

    res = _wrap_if_nullable(res, t.suffix)
    return res


def i_argument(argument: Argument):
    expect_type(argument, Argument)

    argument_type = argument.type
    if isinstance(argument_type, Type):
        return i_type(argument_type)
    elif isinstance(argument_type, TypeWithExtendedAttributes):
        return i_type_with_extended_attributes(argument_type)

    return str(argument_type.type)


def i_operation(o: Operation):
    expect_type(o, Operation)
    return i_type(o.return_type)


def i_interface_member__type_method(member: InterfaceMember):
    expect_type(member, InterfaceMember)
    args = []
    for a in member.arguments:
        expect_type(a, Argument)
        a: Argument
        annotation = i_argument(a)
        if not a.required:
            annotation = _put_annotation_type(annotation, _none)
        g_arg = GArg(a.name, annotation)
        if a.default is not None:
            g_arg.default = i_default(a.default)
        elif not a.required:
            g_arg.default = _none
        args.append(g_arg)

    if isinstance(member.member, Operation):
        returns = i_operation(member.member)
        return GMethod(member.name, arguments=args, returns=returns)

    unhandled(member.member)


def i_interface_member__type_attribute(im: InterfaceMember):
    expect_type(im, InterfaceMember)
    expect_type(im.member, Attribute)

    attribute: Attribute = im.member

    expect_type(attribute.attribute, AttributeRest)
    expect_type(attribute.attribute.type, TypeWithExtendedAttributes)
    return GAttribute(
        im.name,
        i_type_with_extended_attributes(attribute.attribute.type)
    )


def i_interface_member(member: InterfaceMember):
    expect_type(member, InterfaceMember)

    idl_type = member.idl_type

    if idl_type == 'method':
        return i_interface_member__type_method(member)
    if idl_type == 'attribute':
        return i_interface_member__type_attribute(member)

    unhandled(idl_type)


def i_interface(interface: Interface, throw: bool):
    expect_type(interface, Interface)
    members = [i_construct(construct, throw) for construct in interface.members]
    return GInterface(interface.name, bases=interface_bases(interface), body=members)


def i_construct(construct: Construct, throw: bool):
    expect_type(construct, Construct)

    if isinstance(construct, Interface):
        return i_interface(construct, throw)
    if isinstance(construct, InterfaceMember):
        if throw:
            res = i_interface_member(construct)
        else:
            try:
                res = i_interface_member(construct)
            except Exception as ex:
                res = GUnhandled(str(construct), ex)
        return res

    if throw:
        unhandled(construct)
    else:
        return GUnhandled(str(construct), None)


def i_union_member_types(umt: UnionMemberType):
    expect_type(umt, UnionMemberType)
    assert umt.suffix is None
    t = umt.type
    if isinstance(t, NonAnyType):
        return i_non_any_type(t)
    elif isinstance(t, UnionType):
        return i_union_type(t)

    unhandled(t)


def i_union_type(union_type: UnionType):
    ann = [i_union_member_types(a) for a in union_type.types]
    return ann


def ingest(idl: str, throw: bool = True) -> List[GStmt]:
    statements: List[GStmt] = []
    parser = widlparser.Parser()
    parser.markup()
    parser.parse(idl)
    for c in parser.constructs:
        if throw:
            construct = i_construct(c, throw)
        else:
            try:
                construct = i_construct(c, throw)
            except Exception as ex:
                construct = GUnhandled(str(c), ex)
        statements.append(construct)
    return statements


def _m_interface(statements: List[GInterface]) -> GInterface:
    # check pre-conditions
    name = None
    for st in statements:
        expect_type(st, GInterface)
        if name is None:
            name = st.name
        else:
            assert st.name == name

    result = GInterface(name)
    for st in statements:
        result.bases.extend(st.bases)
        result.body.extend(st.body)
    return result


def _put_annotation_type(annotation, param):
    if isinstance(annotation, list):
        if param not in annotation:
            annotation.append(param)
    else:
        annotation = _put_annotation_type([annotation], param)
    return annotation


def _wrap_if_nullable(o, suffix: TypeSuffix | None):
    nullable = suffix is not None
    if nullable:
        o = _put_annotation_type(o, _none)
    return o


def merge(statements: List[GStmt]) -> List[GStmt]:
    unhandled, handled = partition(statements, lambda e: isinstance(e, GUnhandled))
    result: List[GStmt] = []
    by_name = groupby(handled, lambda stmt: stmt.name)
    # { 'Doc' : [ GInterface('Doc', ... ), GInterface('Doc', ...), GSomething('Doc', ...) ] , ... }
    for name, sts_for_name in by_name.items():
        by_type = groupby(sts_for_name, lambda s: type(s))
        # { GInterface : [ ... ] , GSomething : [ ... ] }
        for typ, sts_for_type in by_type.items():
            if typ == GInterface:
                mi = _m_interface(sts_for_type)
                result.append(mi)
            else:
                # don't know how to merge
                result.extend(sts_for_type)
    return result + unhandled


def discard_unhandled_inplace(statements: List[GStmt]) -> List[GStmt]:
    def if_unhandled(e):
        return isinstance(e, GUnhandled)

    remove_inplace(statements, if_unhandled)

    for st in statements:
        remove_inplace(st.body, if_unhandled)

    return statements
