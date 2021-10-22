from Ex3a import bignFunction


def f(x): return x**2-3
a = 1
b = 2
itmax = 10**4
tol = 10**-8
opt = 2

x, y = bignFunction(f, a, b, itmax, tol, opt)

print(x, y)