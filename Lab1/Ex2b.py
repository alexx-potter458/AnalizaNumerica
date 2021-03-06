import matplotlib.pyplot as plt
import numpy as np
import math

def f(x): return (math.e**(-x))*((x**2)-5*x+2) - 1

def bisectMethod(a, b):
    x = a + (b-a)/2
   
    for i in range(10):
        if(f(x)*f(a)) <= 0:
            b = x
        else:
            a = x
        x = a + (b-a)/2
        print(x)
        plt.scatter(x, f(x),s=10, marker='o', color = "red")
        
    plt.scatter(x, f(x),s=50, marker='o', color = "black")

interval = np.linspace(-1,1)
y=f(interval)

plt.plot(interval,y, linewidth=1)
bisectMethod(-1, 1)

plt.axhline(0)
plt.show()
