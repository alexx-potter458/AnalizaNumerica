import numpy as np

def Richardson(f, x, h, n):

    phi = np.zeros((n, n))
    
    for i in range(n):
        phi[i, 0] = f(x, h / 2**i)
    
    for i in range(1,n):
        for j in range(1, i+1):
            phi[i, j] = 1 / (2**j - 1) * (2**j * phi[i, j-1] - phi[i-1, j-1])
            
    return phi[n-1, n-1]