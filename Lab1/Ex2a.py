import matplotlib.pyplot as plt
import numpy as np
from math import e

def g(x): return e**-x*(x**2-5*x+2)

interval = np.linspace(-3,3)
y=g(interval)
plt.plot(interval,y,c='red',linewidth=3)
plt.axvline(0)

