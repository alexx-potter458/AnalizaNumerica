import matplotlib.pyplot as plt
import numpy as np
from Ex3a import NewtonRapson

def f(x): return np.cos(x) - x
def fd(x): return -np.sin(x) - 1

tol = 10**-5
x0 = np.pi/4

solution = NewtonRapson(f,fd, x0, tol)

print("Solution: ", solution)
plt.scatter(x0, solution,s=50, marker='o', color = "red")

rangeX = np.linspace(0,np.pi/2)
y = f(rangeX)


plt.plot(rangeX,y)
plt.axhline(0)
plt.show()