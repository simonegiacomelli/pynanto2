from __future__ import annotations

import widlparser
from widlparser import Interface, InterfaceMember, Construct, TypeWithExtendedAttributes, Argument, UnionType, \
    Attribute, AttributeRest, SingleType, AnyType, NonAnyType, PrimitiveType, Symbol, TypeIdentifier, Default, Type, \
    TypeSuffix, Operation, UnionMemberType, UnsignedIntegerType, UnrestrictedFloatType, Enum, EnumValue, \
    IncludesStatement, Typedef, ExtendedAttribute

from js_pyi.assertions import unhandled, expect_isinstance
from js_pyi.datamodel import *

_none = 'None'


def i_symbol(symbol: Symbol):
    expect_isinstance(symbol, Symbol)
    s = symbol.symbol

    return s


def i_default(default: Default):
    expect_isinstance(default, Default)
    value = default.value
    if '/*' in value:
        unhandled(default)
    return value


def i_type_identifier(ti: TypeIdentifier):
    expect_isinstance(ti, TypeIdentifier)
    return ti.name


def i_primitive_type(primitive_type: PrimitiveType):
    expect_isinstance(primitive_type, PrimitiveType)

    t = primitive_type.type
    if isinstance(t, Symbol):
        return i_symbol(t)
    if isinstance(t, UnsignedIntegerType) or \
            isinstance(t, UnrestrictedFloatType):
        s = str(t)
        return s
    unhandled(t)


def _wrap_if_nullable(o, suffix: TypeSuffix | None):
    nullable = suffix is not None
    if nullable:
        o = _put_annotation_type(o, _none)
    return o


def _wrap_if_generic(res, non_any_type: NonAnyType):
    if non_any_type.promise is not None:
        return GGeneric('Promise', res)
    if non_any_type.sequence is not None:
        return GGeneric('sequence', res)
    return res


def i_non_any_type(non_any_type: NonAnyType):
    expect_isinstance(non_any_type, NonAnyType)

    res = None
    t = non_any_type.type
    if isinstance(t, PrimitiveType):
        res = i_primitive_type(t)
    elif isinstance(t, Type):
        res = i_type(t)
    elif isinstance(t, TypeIdentifier):
        res = i_type_identifier(t)
    elif isinstance(t, Symbol):
        res = i_symbol(t)
    elif isinstance(t, TypeWithExtendedAttributes):
        res = i_type_with_extended_attributes(t)
    else:
        unhandled(t)

    res = _wrap_if_generic(res, non_any_type)
    res = _wrap_if_nullable(res, non_any_type.suffix)

    return res


def i_single_type(single_type: SingleType):
    expect_isinstance(single_type, SingleType)
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


def i_type_with_extended_attributes(twea: TypeWithExtendedAttributes) -> GType:
    expect_isinstance(twea, TypeWithExtendedAttributes)

    t = twea.type
    if isinstance(t, UnionType):
        res = i_union_type(t)
    elif isinstance(t, SingleType):
        res = i_single_type(t)
    else:
        unhandled(t)

    return _wrap_if_nullable(res, twea.suffix)


def i_type(t: Type):
    expect_isinstance(t, Type)

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
    expect_isinstance(argument, Argument)

    argument_type = argument.type
    if isinstance(argument_type, Type):
        return i_type(argument_type)
    elif isinstance(argument_type, TypeWithExtendedAttributes):
        return i_type_with_extended_attributes(argument_type)

    return str(argument_type.type)


def i_operation(o: Operation):
    expect_isinstance(o, Operation)
    return i_type(o.return_type)


def i_interface_member__type_method(member: InterfaceMember):
    expect_isinstance(member, InterfaceMember)
    args = []
    for a in member.arguments:
        expect_isinstance(a, Argument)
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
    expect_isinstance(im, InterfaceMember)
    expect_isinstance(im.member, Attribute)

    attribute: Attribute = im.member

    expect_isinstance(attribute.attribute, AttributeRest)
    expect_isinstance(attribute.attribute.type, TypeWithExtendedAttributes)
    if im.name == 'global' or im.name == 'as':
        unhandled('The keyword `global` cannot be used as a variable name ')
    attributes = i_type_with_extended_attributes(attribute.attribute.type)
    return GAttribute(im.name, attributes)


def i_interface_member(member: InterfaceMember):
    expect_isinstance(member, InterfaceMember)

    idl_type = member.idl_type

    if idl_type == 'method':
        return i_interface_member__type_method(member)
    if idl_type == 'attribute':
        return i_interface_member__type_attribute(member)

    unhandled(idl_type)


def i_interface(interface: Interface, throw: bool):
    expect_isinstance(interface, Interface)
    members = [i_construct(construct, throw) for construct in interface.members]
    return GClass(interface.name, bases=interface_bases(interface), body=members)


def i_enum_value(enum_value: EnumValue):
    return GEnumValue(enum_value.value)


def i_include_statement(i: IncludesStatement):
    expect_isinstance(i, IncludesStatement)
    return GInclude(i.name, i.includes)


def i_enum(enum: Enum):
    expect_isinstance(enum, Enum)
    members = [i_enum_value(value) for value in enum.enum_values]
    return GEnum(enum.name, body=members)


def i_typedef(td: Typedef):
    expect_isinstance(td, Typedef)
    ann = i_type_with_extended_attributes(td.type)
    return GTypedef(td.name, ann)


def i_extended_attribute(construct: ExtendedAttribute):
    expect_isinstance(construct, ExtendedAttribute)
    return GIgnoredStmt(str(construct))


def i_construct(construct: Construct, throw: bool):
    expect_isinstance(construct, Construct)

    if isinstance(construct, Interface):
        return i_interface(construct, throw)
    if isinstance(construct, Enum):
        return i_enum(construct)
    if isinstance(construct, Typedef):
        return i_typedef(construct)
    if isinstance(construct, IncludesStatement):
        return i_include_statement(construct)
    if isinstance(construct, ExtendedAttribute):
        return i_extended_attribute(construct)
    if isinstance(construct, InterfaceMember):
        if throw:
            res = i_interface_member(construct)
        else:
            try:
                res = i_interface_member(construct)
            except Exception as ex:
                res = GUnhandledNested(str(construct), ex)
        return res

    unhandled(construct)


def i_union_member_types(umt: UnionMemberType):
    expect_isinstance(umt, UnionMemberType)
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
                construct = GUnhandledRoot(str(c), ex)
        statements.append(construct)
    return statements


def _put_annotation_type(annotation, param):
    if isinstance(annotation, list):
        if param not in annotation:
            annotation.append(param)
    else:
        annotation = _put_annotation_type([annotation], param)
    return annotation


def keep_python_producer(statements: List[GStmt]) -> List[GStmt]:
    def filter_pp(iterable):
        return list(filter(lambda e: isinstance(e, GPythonProducer), iterable))

    statements = filter_pp(statements)

    for st in statements:
        if hasattr(st, 'body'):
            st.body = filter_pp(st.body)

    return statements


def keep_unhandled(statements: List[GStmt]) -> List[GStmt]:
    def keep_unhand(iterable):
        return list(filter(lambda e: isinstance(e, GUnhandled), iterable))

    for st in statements:
        if hasattr(st, 'body'):
            st.body = keep_unhand(st.body)

    statements = list(filter(
        lambda e: isinstance(e, GUnhandled)
                  or (hasattr(st, 'body') and len(e.body) > 0), statements)
    )

    return statements
