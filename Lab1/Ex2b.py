import matplotlib.pyplot as plt
import numpy as np
from math import e

def g(x): return e**-x*(x**2-5*x+2)

def metbis(a, b, i) :
    x = a + (b-a)/2
    for j in range(i):
        
        if g(a) * g(x) <=0:     
            b = x
        else:
            a = x       
        x = a + (b-a)/2
        print (j)
    return x

a, b = -3, 3
def g(x): return np.exp(-x)*(x**2-5*x+2)-1
x = np.linspace(a,b)
y = g(x)
plt.plot(x,y, c="green" ,linewidth = 0.5)
plt.axhline(0, c='purple')
x = metbis(-1,1, 10)
print(x)
plt.scatter(x, g(x), s=50, c='brown', marker='o')