def Steffensen(f, phi, xn, itmax, tol):
    iterations = 0
    print("Starting Steffensen:")
    xNew = phi(xn)
    xNewest = phi(xNew)
    while abs(f(xn)) >= tol and iterations < itmax:
        iterations += 1
        xn = (xNewest*xn - xNew**2) / (xNewest - 2*xNew + xn)
        xNew = phi(xn)
        xNewest = phi(xNew)
        print("%d. xn=%.10f -- errAbs=%.4e --  errRel=%.4e -- f(xn)=%.4e -- tol=%.4e" % (iterations, xn, abs(xNewest-xNew), abs((xNewest-xNew)/xNew), abs(f(xn)), tol))

    return [xn, iterations]