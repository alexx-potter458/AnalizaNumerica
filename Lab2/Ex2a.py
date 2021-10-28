import matplotlib.pyplot as plt
import numpy as np
import math

rangeX = np.linspace(-1,1)

def f(x): return (x + ((math.e)**(-x**2)) * np.cos(x))
def fd(x): return (1 + (-math.e**(-x**2))*np.sin(x) - 2*x*(math.e**(-x**2))*np.cos(x))
y = f(rangeX)

plt.plot(rangeX,y)


plt.axhline(0)
plt.show()