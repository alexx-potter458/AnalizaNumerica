import numpy as np
import math
import Ex1b as algorithms

def f(x): return x + math.e**(-x**2)*np.cos(x)


algorithms.Secantaf(f, -1, 1, 10)
algorithms.PozitieFalsaf(f, -1, 1, 10)
print()
print()
algorithms.Secantaf(f, 1, -1, 10)
algorithms.PozitieFalsaf(f, 1, -1, 10)