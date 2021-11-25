import numpy as np

def SplinePatratic(f,a,b,n,x,fd):
    xDivs = np.linspace(a,b,n+1)
    h = xDivs[1]-xDivs[0]
    yDivs = f(xDivs)
    a = np.zeros(n)
    for j in range(n):
        a[j] = yDivs[j]
        
    M = np.zeros((2*n,2*n))
    M[0][0] = 1
    t = np.zeros(2*n)
    t[0] = fd

    for j in range(n-1):
        t[2*j+1] = yDivs[j+1] - yDivs[j]
        M[2*j+1,2*j+1] = h**2
        M[2*j+1,2*j] = h
        
        M[2*j+2,2*j+2] = -1
        M[2*j+2,2*j+1] = 2*h
        M[2*j+2,2*j] = 1
        
    j = n-1
    t[2*j+1] = yDivs[j+1] - yDivs[j]
    M[2*j+1,2*j+1] = h**2
    M[2*j+1,2*j] = h
        
    bc = np.linalg.solve(M,t)
    b = bc[0:2*n:2]
    c = bc[1:2*n:2]

    for j in range(n):

        if xDivs[j] <= x <= xDivs[j+1]:
            y = a[j] + b[j] * (x - xDivs[j]) + c[j] * (x - xDivs[j])**2
            
            return y