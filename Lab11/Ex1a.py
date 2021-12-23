import numpy as np

def CuadMetCoefNedet(f,a,b,n):
    x=np.linspace(a,b,n+1)
    A=np.zeros((n+1,n+1))
    B=np.zeros(n+1)
    for i in range(n+1):
        A[i,:]=x**i
        B[i]=(b**(i+1)-a**(i+1))/(i+1)
    w=np.linalg.solve(A,B)
    I=0
    for i in range(n+1):
        I=I+f(x[i])*w[i]
    return I