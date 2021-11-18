import numpy as np
import matplotlib.pyplot as plt
from Ex1a import MetBaricentrica

def f(x): return 1/(1 + 12*(x**2))
a = -1
b = 1
x = np.linspace(a, b)
n = [13]
Pn = []
#b1
for nn in n:
    pn = []
    for i in x:
        pn.append(MetBaricentrica(f, a, b, nn, i))
    Pn.append(pn)

#b2
plt.plot(x, f(x))
for i in Pn:
    plt.plot(x, i, linestyle="--")

#b3
plt.figure()
def errAbs(y, yp): return abs(y-yp)
for i in Pn:
    errs = errAbs(f(x), i)
    plt.plot(x, errs)

plt.show()
