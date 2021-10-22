import matplotlib.pyplot as plt
import numpy as np

def f(x): return x**6-x-1

interval = np.linspace(-2,2)
y=f(interval)

plt.plot(interval,y,c='purple',linewidth=3)
plt.axhline(0)
