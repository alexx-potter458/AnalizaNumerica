import numpy as np
import Ex2a as algorithms
import matplotlib.pyplot as plt


def f(x): return np.cos(x) - x
x0 = 0
x1 = np.pi/2
tol = 10**-10

rangeX = np.linspace(x0, x1)
y = f(rangeX)

plt.plot(rangeX, y)

xpf = algorithms.PozitieFalsaf(f,x0, x1, tol)
xs = algorithms.Secantaf(f,x0, x1, tol)

ypf = f(xpf)
ys = f(xs)
plt.plot(xpf, ypf)
plt.plot(xs, ys)

print()

xpf = algorithms.PozitieFalsaf(f,x1, x0, tol)
xs = algorithms.Secantaf(f,x1, x0, tol)

ypf = f(xpf)
ys = f(xs)
plt.plot(xpf, ypf)
plt.plot(xs, ys)



plt.axhline(0)
plt.show()