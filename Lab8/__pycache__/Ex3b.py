import numpy as np
import matplotlib.pyplot as plt
from Ex3a import SplineCubic

def f(x): return np.exp(2*x)

a = -1
b = 1
n = 5
x = np.linspace(a, b)
Sn = []

for xi in x:
    Sn.append(SplineCubic(f, a, b, n, xi))

plt.title('Spline cubic')
plt.plot(x, f(x))
plt.plot(x, Sn, linestyle="--")

plt.figure()

plt.title('Eroare spline cubic')
def errAbs(y, yp): return abs(y-yp)
errs = errAbs(f(x), Sn)
plt.plot(x, errs)

plt.show()
