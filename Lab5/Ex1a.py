import numpy as np
import matplotlib.pyplot as plt

def MetNaiva(f, a, b, n, x):
    X = np.linspace(a, b, n + 1)
    Y = f(X)
    plt.scatter(X, f(X), s=100, c='blue', edgecolors = 'k', marker='o')
    
    A = np.vander(X, n + 1)
    C = np.linalg.solve(A, Y)
    C = np.flip(C)

    Pn = np.zeros(len(x))

    for j in range(len(x)):
        y = 0
        for i in range(n+1):
            y = y + C[i]*x[j]**i
        Pn[j] = y
    
    return Pn