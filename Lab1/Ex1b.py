import matplotlib.pyplot as plt
import numpy as np

tol = 10**-5

def f(x): return  x**6-x-1

def bisectMethod(a, b):
    x = a + (b-a)/2
   
    while abs(f(x)) >= tol:
        if(f(x)*f(a)) <= 0:
            b = x
        else:
            a = x
        x = a + (b-a)/2
        print(x)
        plt.scatter(x, f(x),s=10, marker='o', color = "red")

    plt.scatter(x, f(x),s=50, marker='o', color = "black")

firstInterval = np.linspace(-1,0)
plt.plot(firstInterval, f(firstInterval), c='blue')
bisectMethod(-1, 0)

secondInterval = np.linspace(1,2)
plt.plot(secondInterval, f(secondInterval), c='red')
bisectMethod(1, 2)

plt.axhline(0)
plt.show()