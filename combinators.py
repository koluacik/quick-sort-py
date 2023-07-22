# Use these to look smart
S = lambda f: lambda g: lambda x: f(x)(g(x))
K = lambda x: lambda _: x
I = lambda x: x
M = lambda x: x(x)
OMEGA = lambda x: M(x)(M(x))
Y = lambda f: M(lambda y: f(lambda x: M(y)(x)))

Compose = lambda f: lambda g: lambda x: f(g(x))
Flip = lambda f: lambda x: lambda y: f(y)(x)
Apply = lambda f: lambda x: f(x)

Repeat = lambda n: lambda f: n(f)
