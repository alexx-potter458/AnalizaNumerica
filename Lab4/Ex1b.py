def NewtonRapsonModificata1(m, f, fd, xn, itmax, tol):
    iterations = 0
    print("Starting NewtonRapsonModified1:")
    
    while abs(f(xn)) >= tol and iterations < itmax:
        iterations+=1
        xOld = xn
        xn = (xn - m*f(xn)/fd(xn))
        print("%d. xn=%.10f -- err=%.4e -- f(xn)=%.4e -- tol=%.4e" % (iterations, xn, abs(xn-xOld), f(xn), tol))

    return [xn, iterations]



def f(x): return x**3 - 4*x**2 + 5*x - 2
def fd(x): return 3*x**2 - 8*x + 5
tol = 10**-10
x0 = 0
itmax = 10
result = NewtonRapsonModificata1(2, f, fd,x0 ,itmax, tol)

print(result)