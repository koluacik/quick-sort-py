from combinators import *

TRUE = K
FALSE = Flip(K)


def interpret_bool(b):
    return b(True)(False)


IF_THEN_ELSE = lambda b: lambda if_t: lambda if_f: b(if_t)(if_f)

AND = lambda l: lambda r: l(r(TRUE)(FALSE))(FALSE)

OR = lambda l: lambda r: l(TRUE)(r(TRUE)(FALSE))

NOT = Flip
