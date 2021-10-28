from Ex2b import Steffensen
from Ex2a import Aitken

def NewtonRaphson(f, fd, xn, itmax, tol):
    iterations = 0
    print("Starting NewtonRapson:")
    while abs(f(xn)) >= tol and iterations < itmax:
        iterations+=1
        xOld = xn
        xn = (xn - f(xOld)/fd(xOld))
        print("%d. xn=%.10f -- err=%.4e -- f(xn)=%.4e -- tol=%.4e" % (iterations, xn, abs(xn-xOld), f(xn), tol))

    return [xn, iterations]

def f(x): return x**3 - 4*x**2 + 5*x - 2
def fd(x): return 3*x**2 - 8*x + 5
def phi(x): return x - f(x)/fd(x)
tol = 10**-10
x0 = 0
itmax = 20

Aitken(f, phi, x0, itmax, tol)
Steffensen(f, phi, x0, itmax, tol)
NewtonRaphson(f, fd, x0, itmax, tol)
