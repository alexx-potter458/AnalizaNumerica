import numpy as np
import matplotlib.pyplot as plt

from Ex1a import MetNaiva

def f(x): return np.exp(2*x)
a = -1
b = 1
n = 3
x = np.linspace(a, b)


#b1
yMetNaiva = MetNaiva(f, a , b , n, x)
# print(yMetNaiva)

#b2
# plt.plot(x, f(x))
# plt.plot(x, yMetNaiva, linestyle="--")

#b3
def errAbs(y, yp): return abs(y-yp)
errs = errAbs(f(x), yMetNaiva)
plt.scatter(x, errs)

plt.show()