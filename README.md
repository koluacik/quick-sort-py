# Quick sort with λ

We all know that lambda calculus is equivalent to Turing machines in terms of computational power. Thanks to this, functional programmers can implement algorithms they learned in their undergrad algorithms course using their favourite programming languages. We just need to make a few adjustments to our code such as:
- `car`/`cdr` instead of `std::pair<T1,T2>.first`, or
- `if-then-else` conditional expressions instead of conditional statements, or
- `λf. (λx. f (x x))(λx. f (x x))` fixed-point combinator instead of `for` loops

all of which should be fairly trivial to the reader.

Given this, this repo aims to demonstrate merits of programming style with rich lambda presence. Every programming construct used in this repo, including natural numbers, arithmetic operators, boolean constants, boolean operators, conditional expressions, basic data structures such as pairs and more exotic concepts such as lists and higher order functions (don't forget, lists and map/filter are the 🍞 and butter of functional programmers), is implemented purely using lambda calculus encodings.

One problem with untyped lambda calculus is that it is untyped. You need to know how to interpret a lambda term. The same term can be interpreted as `0`, `False`, `snd` as in Haskell's `snd`, or `cdr` depending on the context. With great power, comes great responsibility!

# Examples
```py
>>> interpret_nat(pow(s(s(s(z))))(s(s(s(z)))))
27

>>> interpret_pair(mk_pair(TRUE)(nats[3]), interpret_bool, interpret_nat)
(True, 3)

>>> interpret_bool(S(I)(K)((I)(K))(TRUE)(FALSE))
True

>>> interpret_list_nat(lst4)
[0, 1, 3, 5, 0, 10, 9, 8, 7, 6, 10, 9, 8, 7, 6, 99]

>>> interpret_list_nat(qsort(lst4))
[0, 0, 1, 3, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 99]

>>> interpret_nat(uncurry(lambda l: lambda r: cmp(l)(r)(nats[10])(nats[20])(nats[30]))(mk_pair(nats[55])(nats[55])))
20

>>> interpret_list_nat(map_(Flip(pow)(nats[2]))(lst4))
[0, 1, 9, 25, 0, 100, 81, 64, 49, 36, 100, 81, 64, 49, 36, 9801]
```