from combinators import *
from bool import *

# elements of mk_pair(x)(y) can be accessed with projection function p
# mk_pair(x)(y)(K) = x etc.
mk_pair = lambda l: lambda r: lambda p: p(l)(r)

# Flip(Apply) looks stupid.
fst = Flip(Apply)(K)  # Pretend this one is ($ K)
snd = Flip(Apply)(Flip(K))


def interpret_pair(lam, l_interpreter, r_interpreter):
    return (l_interpreter(fst(lam)), r_interpreter(snd(lam)))


uncurry = lambda f: lambda p: f(fst(p))(snd(p))
curry = lambda f: lambda l: lambda r: f(mk_pair(l)(r))

nil = K(K)
cons = mk_pair
car = fst
cdr = snd
null = Flip(Apply)(K(K(Flip(K))))  # lambda p: p (lambda x: lambda y: FALSE)


def interpret_list(lam, val_interpreter):
    nil_ = []
    return list(
        reversed(
            reduce(lambda v: lambda acc: (acc.append(val_interpreter(v)), acc)[1])(
                nil_
            )(lam)
        )
    )


# lambdas in then/else parts ensure lazy evaluation
map_ = lambda f: lambda l: (
    IF_THEN_ELSE(null(l))(lambda: nil)(lambda: cons(f(car(l)))(map_(f)(cdr(l))))
)()

filter_ = lambda p: lambda l: (
    IF_THEN_ELSE(null(l))(lambda: nil)(
        lambda: (IF_THEN_ELSE(p(car(l)))(cons(car(l)))(I))(filter_(p)(cdr(l)))
    )
)()

reduce = lambda f: lambda i: lambda l: (
    IF_THEN_ELSE(null(l))(lambda: i)(lambda: f(car(l))(reduce(f)(i)(cdr(l))))
)()

concat = Flip(reduce(lambda v: lambda acc: cons(v)(acc)))
