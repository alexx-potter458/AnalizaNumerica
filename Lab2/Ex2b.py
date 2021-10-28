import numpy as np
import math

def NewtonRapson(f, fd, xn, N):
    iterations =[]
    iterations.append(xn)

    for i in range(N):
        xn = (xn - f(xn)/fd(xn))
        iterations.append(xn)
    
    return iterations

def f(x): return (x + ((math.e)**(-x**2)) * np.cos(x))
def fd(x): return (1 + (-math.e**(-x**2))*np.sin(x) - 2*x*(math.e**(-x**2))*np.cos(x))

iterations = NewtonRapson(f, fd, 0, 10)

for i in iterations:
    print(i)