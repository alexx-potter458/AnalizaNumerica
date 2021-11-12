import numpy as np
import matplotlib.pyplot as plt
from Ex2a import MetNewton

def f(x): return np.exp(2*x)
a = -1
b = 1
x = np.linspace(a, b, 52)
n = [1, 2, 3, 4]
Pn = []
#b1
for nn in n:
    pn = []
    X = np.linspace(a, b, nn+1)
    Y = f(X)
    for i in x:
        pn.append(MetNewton(f, X, Y, nn, i))
    print(pn)
    Pn.append(pn)

#b2
plt.plot(x, f(x))
for i in Pn:
    plt.plot(x, i, linestyle="--")

# b3
plt.figure()
def errAbs(y, yp): return abs(y-yp)
for i in Pn:
    errs = errAbs(f(x), i)
    plt.scatter(x, errs)

plt.show()
