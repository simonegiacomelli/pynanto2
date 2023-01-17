from dataclasses import dataclass
from typing import List, Tuple, Any

import widlparser
from widlparser import Construct, Interface, InterfaceMember

dc = dataclass()


@dc
class GAst: ...


@dc
class GExpr(GAst): ...


@dc
class GStmt(GAst): ...


@dc
class GWithName:
    name: str


@dc
class GName:
    name: str


@dataclass()
class GClassDef:
    name: str
    bases: List[GName] = ()
    body: List[GStmt] = ()


@dataclass
class GArguments:
    posonlyargs: Tuple[Any] = ()
    args: Tuple[Any] = ()
    vararg: Tuple[Any] = ()
    kwonlyargs: Tuple[Any] = ()
    kw_defaults: Tuple[Any] = ()
    kwarg: Tuple[Any] = ()
    defaults: Tuple[Any] = ()


@dataclass
class GArg:
    name: str
    annotation: GName


@dataclass
class GFunctionDef:
    name: str
    arguments: GArguments
    returns: GArg


class GModule(List[GStmt]):
    pass


def generate(idl: str) -> GModule:
    widl = widlparser.Parser()
    widl.parse(idl)
    processor = Processor()
    result = GModule()
    for c in widl.constructs:
        result.append(processor.process(c))
    return result


def remove_none(param):
    return [m for m in param if m is not None]


class Processor:
    def __init__(self):
        pass

    def c_interface(self, c: Interface):
        members = remove_none(self.process_member(m) for m in c.members)

        return GClassDef(c.name, bases=[c.inheritance.base], body=members)

    def c_InterfaceMember(self, member: InterfaceMember):
        args = []
        for a in member.arguments:
            args.append(
                GArg(a.name, GName(str(a.type.type)))
            )
        if isinstance(member.member, widlparser.Operation):
            returns = GName(str(member.member.return_type).strip())
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
