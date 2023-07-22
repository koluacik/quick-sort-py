from data_structures import *
from nat import *
from combinators import *
from bool import *

# example lists
lst1 = cons(z)(cons(s(z))(nil))
lst2 = cons(nats[3])(cons(nats[5])(cons(nats[0])(nil)))
lst3 = cons(nats[10])(cons(nats[9])(cons(nats[8])(cons(nats[7])(cons(nats[6])(nil)))))
lst4 = concat(lst1)(concat(lst2)(concat(lst3)(concat(lst3)(cons(nats[99])(nil)))))

# should be obvious and intuitive
qsort = Y(
    lambda f: lambda l: (
        IF_THEN_ELSE(null(l))(lambda: nil)(
            lambda: concat(f(filter_(Flip(lt)(car(l)))(cdr(l))))(
                concat(cons(car(l))(nil))(f(filter_(Flip(ge)(car(l)))(cdr(l))))
            )
        )
    )()
)
