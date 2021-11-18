import numpy as np
import sympy as sym

def MetHermite_sym(f,df,a,b,n,x):

    xd=np.linspace(a,b,n+1)
    yd=f(xd)
    dyd=df(xd)

    t=sym.symbols('t')
    P=0*t
    for k in range(n+1):
        L=1+0*t
        for i in range(n+1):
            if i!=k:
                L=L*(t-xd[i])/(xd[k]-xd[i])
        dL=sym.diff(L)
        H=L**2*(1-2*dL.subs(t,xd[k])*(t-xd[k]))
        K=L**2*(t-xd[k])
        P=P+yd[k]*H+dyd[k]*K
    y=P.subs(t,x)
    return y, P