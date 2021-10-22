import matplotlib.pyplot as plt
import numpy as np

# def metPuntFix(phi, a, b):


def f(x):
    return -x**3-4*x**2-10
def fPrim(x):
    return -3*x**2-8*x

interval = np.linspace(1,2)
y=f(interval)
yPrim = fPrim(interval)
plt.plot(interval,y,c='red',linewidth=3)
plt.plot(interval,yPrim,c='green',linewidth=3)