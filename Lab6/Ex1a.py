import numpy as np

def MetNeville(f, a, b, n, x):
    
    X = []
    Q = np.zeros((n+1, n+1))

    h = (b-a)/n
    for i in range(n+1):
        X.append((a + i * h))
        Q[i,0] = f(X[i])
    Pn = 0

    for i in range(1,n+1):
        for j in range(1,i+1):
            Q[i,j] = (Q[i,j-1]*(x - X[i-j]) - Q[i-1,j-1]*(x - X[i])) / (X[i] - X[i-j])
         
    Pn = Q[n,n]
    return Pn
