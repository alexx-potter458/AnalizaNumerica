import numpy as np
import matplotlib.pyplot as plt

def MetLagrange(f, a, b, n, x):
    X = np.linspace(a, b, n + 1)
    Y = f(X)
    plt.scatter(X, f(X), s=100, c='blue', edgecolors = 'k', marker='o')
    
    A = np.vander(X, n + 1)
    C = np.linalg.solve(A, Y)
    C = np.flip(C)

    Pn = np.zeros(len(x))

    for i in range(len(x)):
        y = 0
        for j in range(n+1):
            val=1
            
            for k in range(n+1):
                if k!=j:
                    val*=(x[i]-X[k])/(X[j]-X[k])
            
            y += val*Y[j]
            
        Pn[i] = y
    return Pn