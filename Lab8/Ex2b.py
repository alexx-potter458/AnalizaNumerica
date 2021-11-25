import numpy as np
import matplotlib.pyplot as plt
from Ex2a import SplinePatratic

def f(x): return np.exp(2*x)
def fd(x): return 2*np.exp(2*x)
a = -1
b = 1
n = 5
x = np.linspace(a, b)
Sn = []

for xi in x:
    Sn.append(SplinePatratic(f, a, b, n, xi, fd(a)))

plt.title('Spline patratic')
plt.plot(x, f(x))
plt.plot(x, Sn, linestyle="--")

plt.figure()

plt.title('Eroare spline patratic')
def errAbs(y, yp): return abs(y-yp)
errs = errAbs(f(x), Sn)
plt.plot(x, errs)

plt.show()
