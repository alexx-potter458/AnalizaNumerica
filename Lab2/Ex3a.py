def NewtonRapson(f, fd, xn, tol):
    while abs(f(xn)) >= tol:
        xn = (xn - f(xn)/fd(xn))

    return xn
