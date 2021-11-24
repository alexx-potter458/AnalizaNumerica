import numpy as np
import matplotlib.pyplot as plt
from Ex1a import MetBaricentrica

def f(x): return 1/(1 + 12*(x**2))
a = -1
b = 1
x = np.linspace(a, b)
n = [1, 2, 3, 4, 6, 8, 10]
Pn = []

for nn in n:
    pn = []
    for i in x:
        pn.append(MetBaricentrica(f, a, b, nn, i))
    Pn.append(pn)

for i in Pn:
    plt.figure()
    plt.plot(x, f(x))
    plt.plot(x, i, linestyle="--")
    
plt.show()
