import matplotlib.pyplot as plt
import numpy as np 

tol=10**-5
y = lambda x: x**6-x-1
def MetBisect(f,a,b):
    if f(a)*f(b) >= tol:
        print("Ec nu are solutii")
        return None
    x=(a+b)/2
    while f(x)>tol:
        if f(x)*f(a)<=tol:
            b=x
        else:
            a=x
        x=(a+b)/2
        print(x)
        plt.scatter(x,f(x),s=100)  
        
plt.plot(-1.0,0.0)
plt.axhline(0)
        
MetBisect(y,-1.0,0.0)