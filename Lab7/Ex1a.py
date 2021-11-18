import numpy as np

def MetBaricentrica(f,a,b,n,x):

    xd=np.linspace(a,b,n+1)

    for k in range(n+1):
        xd[k]=(a+b)/2+(b-a)/2*np.cos(k*np.pi/n)

    yd=f(xd)
    w=np.ones(n+1)
    p=1
    y=0

    for k in range(n+1):
        for i in range(n+1):
            if i!=k:
                w[k]=w[k]/(xd[k]-xd[i])

        p=p*(x-xd[k])
        y=y+(w[k]*yd[k])/(x-xd[k])    

    y=y*p

    return y