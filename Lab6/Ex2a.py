
def MetNewton(f, X, Y, n, x):
    y = Y[0]
    p = 1

    for k in range(1, n+1):
        Pnum = 1
        for i in range(k):
            Pnum *= (X[k] - X[i])
        
        PkOld = MetNewton(f, X, Y, k-1, X[k])
        
        ck = (Y[k] - PkOld)/Pnum
        p *= (x - X[k-1])
        y += ck*p
        
    return y
