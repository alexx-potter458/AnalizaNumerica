import matplotlib.pyplot as plt
import math

xStar = 0.16890435790252071258817243635127

def f(x): return (math.e**(-x))*((x**2)-5*x+2) - 1
def erra(xn): return abs(xStar-xn)
def errn(xn): return abs(xStar - xn)/xStar

def bisectMethod(a, b):
    x = a + (b-a)/2
   
    for i in range(1,10):
        if(f(x)*f(a)) <= 0:
            b = x
        else:
            a = x
        x = a + (b-a)/2
        plt.scatter(i, erra(x),s=10, marker='o', color = "red")
        plt.scatter(i, errn(x),s=10, marker='o', color = "blue")
        


bisectMethod(-1, 1)

plt.axhline(0)
plt.show()
