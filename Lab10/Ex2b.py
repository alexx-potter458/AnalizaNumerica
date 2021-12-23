import numpy as np
from Ex2a import DreptunghiSumat, SimpsonSumat, TrapezSumat, NewtonSumat
def f(x): return np.exp(-x**2)
a = 0
b = 1
m = 5

iDreptunghi = DreptunghiSumat(f, a, b, m)
iTrapez = TrapezSumat(f, a, b, m)
iSimpson = SimpsonSumat(f, a, b, m)
iNewton = NewtonSumat(f, a, b, m)

print('Dreptunghi:', iDreptunghi)
print('Trapez:    ', iTrapez)
print('Simpson:   ', iSimpson)
print('Newton:    ', iNewton)