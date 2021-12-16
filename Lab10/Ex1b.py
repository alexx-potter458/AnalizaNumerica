import numpy as np
from Ex1a import Dreptunghi, Simpson, Trapez, Newton
def f(x): return np.exp(-x**2)
a = 0
b = 1

iDreptunghi = Dreptunghi(f, a, b)
iTrapez = Trapez(f, a, b)
iSimpson = Simpson(f, a, b)
iNewton = Newton(f, a, b)

print('Dreptunghi:', iDreptunghi)
print('Trapez:    ', iTrapez)
print('Simpson:   ', iSimpson)
print('Newton:    ', iNewton)