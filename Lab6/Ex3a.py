import numpy as np

def MetNewtonDD(f, a, b, n, x):
    
    X = []
    Q = np.zeros((n+1, n+1))
    

    h = (b-a)/n
    for i in range(n+1):
        X.append((a + i * h))
        Q[i,0] = f(X[i])

    Pn = f(X[0])
    p = 1
    for k in range(1,n+1):
        ck = 0

        for i in range(k+1):
            p2 = 1
            for j in range(k+1):
                if i!=j:
                    p2 *= (X[i] - X[j])

            ck += f(X[i])/p2

        p *= (x - X[k-1])

        Pn += ck*p

    return Pn
