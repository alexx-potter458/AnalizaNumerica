import matplotlib.pyplot as plt
import numpy as np
import math

def Secantaf(f, a, b, itmax):
    solution = []
    errors = []
    xOld = a
    xn = b

    for i in range(itmax):
        aux = xn
        if f(xn) == f(xOld):
            break
        xn = xn - f(xn)*((xn-xOld) / (f(xn)-f(xOld)))
        xOld = aux
        solution.append(xn)
        errors.append(abs((xn-xOld)/xOld))
    return solution, errors

def PozitieFalsaf(f, a, b, itmax):
    solution = []
    errors = []
    xOldest = a
    xOld = b
    xn = b - f(a)*((b-a) / (f(b)-f(a)))

    for i in range(itmax):
        aux = xn
        aux2 = xOld
        if xn*xOld <= 0:
            if f(xn) == f(xOld):
                break
            xn =xn - f(xn)*((xn-xOld) / (f(xn)-f(xOld)))
        else:
            if f(xn) == f(xOldest):
                break
            xn =xn - f(xn)*((xn-xOldest) / (f(xn)-f(xOldest)))
            
        xOld = aux
        xOldest = aux2
        solution.append(xn)
        errors.append(abs((xn-xOld)/xOld))

    return solution, errors


def f(x): return x + math.e**(-x**2)*np.cos(x)

s, errs = Secantaf(f, 1, -1, 10)
p, errp = PozitieFalsaf(f, 1, -1, 10)
plt.plot(s, errs, color="gray", marker="o", linewidth=4)
plt.plot(p, errp, color="pink", marker="o", linewidth=2)

rangeX = np.linspace(-1,1)
y = f(rangeX)
plt.plot(rangeX, y, color="red")

plt.axhline(0)
plt.show()