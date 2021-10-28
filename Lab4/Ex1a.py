import matplotlib.pyplot as plt
import numpy as np

def f(x): return x**3 - 4*x**2 + 5*x - 2
def fd(x): return 3*x**2 - 8*x + 5

rangeX = np.linspace(0, 1.75)

y = f(rangeX)
yd = fd(rangeX)

plt.plot(rangeX, y, color="blue")
plt.plot(rangeX, yd, color="red")

plt.axhline(0)
plt.show()