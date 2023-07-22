import itertools as it

from bool import *
from combinators import *
from data_structures import *

# Basic intuition: natural numbers are encoded as functions
# nat(f, base) = f(f(f(..(base)..)) where f is an offset function
# nat(lambda x: x + 1, 0) evaluates to the actual value of an encoding
z = lambda f: lambda x: x


def interpret_nat(lam):
    return lam(lambda x: x + 1)(0)


def represent_nat(lam):
    expr = lam(lambda e: f"s({e})")("z")
    return f"lambda f: lambda x: {expr}"


# The successor of n is just applying the offset function f to n
# i.e. if 3 = f(f(f(z))), then 4 is f(f(f(f(z))))
s = lambda n: lambda f: lambda x: f(n(f)(x))

# Let's define some nats
nats = list(it.accumulate(it.repeat(z, 100), lambda l, _: s(l)))

# Change the "base" of LHS from x to r(f)(x).
# That way, the interpreted value is the value of RHS incremented
# by 1 the value of LHS many times.
plus = lambda l: lambda r: lambda f: lambda x: l(f)(r(f)(x))

# Like plus, but instead of changing the base, change offset function f to r(f).
# By doing so, the interpreted value is zero incremented by the value of RHS
# LHS many times.
times = lambda l: lambda r: lambda f: lambda x: l(r(f))(x)

# Or you can reuse plus, this is essentially applying + r to zero l many times
times2 = lambda l: lambda r: l(plus(r))(z)

# same as times2
pow = lambda l: lambda r: r(times(l))(s(z))

# base value is False and the offset function is constant-true :)
is_zero = lambda n: n(K(FALSE))(TRUE)

shift_incr = lambda p: mk_pair(snd(p))(s(snd(p)))

# shift_incr n many times, project fst
dec = lambda n: fst(n(shift_incr)(mk_pair(z)(z)))

# is (lambda: _)() cheating? I don't think so.
cmp = Y(
    lambda f: lambda l: lambda r: lambda lt: lambda eq: lambda gt: (
        IF_THEN_ELSE(AND(is_zero(l))(is_zero(r)))(lambda: eq)(
            IF_THEN_ELSE(is_zero(l))(lambda: lt)(
                IF_THEN_ELSE(is_zero(r))(lambda: gt)(
                    lambda: f(dec(l))(dec(r))(lt)(eq)(gt)
                )
            )
        )
    )()  # Learn how to create on demand lazy evaluation with this simple trick!
)

gt = lambda l: lambda r: cmp(l)(r)(FALSE)(FALSE)(TRUE)
ge = lambda l: lambda r: cmp(l)(r)(FALSE)(TRUE)(TRUE)
lt = lambda l: lambda r: cmp(l)(r)(TRUE)(FALSE)(FALSE)
le = lambda l: lambda r: cmp(l)(r)(TRUE)(TRUE)(FALSE)
eq = lambda l: lambda r: cmp(l)(r)(FALSE)(TRUE)(FALSE)
ne = lambda l: lambda r: cmp(l)(r)(TRUE)(FALSE)(TRUE)


def interpret_list_nat(l):
    return interpret_list(l, interpret_nat)
