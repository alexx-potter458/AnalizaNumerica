import matplotlib.pyplot as plt
import numpy as np 

tol=10**-5

def f(x): return  x**6-x-1

def metBis(f, a, b):
    x = a + (b-a)/2
    while f(x) >= tol:
        if(f(x)*f(a)) <= 0:
            b = x
        else:
            a = x
        x = a + (b-a)/2
        print(x)
        plt.scatter(x, f(x))

# def MetBisect(f,a,b):
#     if f(a)*f(b) >= tol:
#         print("Ec nu are solutii")
#         return None
#     x=(a+b)/2

#     while f(x)>tol:
#         if f(x)*f(a)<=tol:
#             b=x
#         else:
#             a=x
#         x=(a+b)/2
#         print(x)
#         plt.scatter(x,f(x),s=100)  
          
# plt.plot(-1.0,0.0)
# plt.axhline(0)
        
# MetBisect(y,-1.0,0.0)