def Aitken(f, phi, xn, itmax, tol):
    print("Starting Aitken:")
    iterations = 0
    xCap = 0
    xOld = xn
    xn = phi(xOld)
    while abs(f(xCap)) >= tol and iterations < itmax:
        iterations += 1
        xOldest = xOld
        xOld = xn
        xn = phi(xOld)

        xCap = (xn*xOldest - xOld**2) / (xn - 2*xOld + xOldest)
        print("%d. Xn=%.10f - xn=%.10f -- errAbs=%.4e --  errRel=%.4e -- f(xn)=%.4e -- tol=%.4e" % (iterations, xCap, xn, abs(xn-xOld), abs((xn-xOld)/xOld), abs(f(xn)), tol))



    return [xCap, iterations]