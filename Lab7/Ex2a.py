import numpy as np
import sympy as sym

def MetHermite(f,fd,a,b,n,x):

    xDivs = np.linspace(a,b,n+1)
    yDivs = f(xDivs)
    ydDivs = fd(xDivs)

    t = sym.symbols('t')
    P = 0*t

    for k in range(n+1):
        Lnk = 1 + 0*t
        
        for i in range(n+1):
            if i != k:
                Lnk = Lnk * (t - xDivs[i]) / (xDivs[k] - xDivs[i])

        LD = sym.diff(Lnk)

        Hnk = Lnk**2 * (1-2 * LD.subs(t, xDivs[k]) * (t - xDivs[k]))
        Knk = Lnk**2 * (t - xDivs[k])
        
        P = P + yDivs[k] * Hnk + ydDivs[k] * Knk
    
    y = P.subs(t,x)
    return y