import matplotlib.pyplot as plt
import numpy as np
import math

def f(x): return x + math.e**(-x**2)*np.cos(x)
rangeX = np.linspace(-1,1)
y = f(rangeX)

plt.plot(rangeX, y, color="red")

plt.axhline(0)
plt.show()
