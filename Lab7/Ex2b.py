import numpy as np

def MetHermiteDD(f,fd,a,b,n,x):
    
    xDivs=np.linspace(a,b,n+1)
    yDiv=fd(xDivs)

    z = np.zeros(2*n+2)
    z[0:2*n+2:2] = xDivs
    z[1:2*n+2:2]=xDivs

    Dn = np.zeros((2*n+2, 2*n+2))
    Dn[:, 0] = f(z)
    Dn[1:2*n+2:2, 1] = yDiv

    for i in range(2, 2*n+2, 2):
        Dn[i][1] = (Dn[i][0] - Dn[i-1][0]) / (z[i] - z[i-1])   

    for i in range(2, 2*n+2):
        for j in range(2, i+1):
            Dn[i][j]=(Dn[i][j-1] - Dn[i-1][j-1]) / (z[i] - z[i-j])

    y = Dn[0,0]
    p = 1
    for k in range(1, 2*n+2):
        p = p * (x - z[k-1])
        y = y + Dn[k][k] * p
    
    return y