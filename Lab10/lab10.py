# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:59:09 2021

@author: Andreea Grecu
"""
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#%% continuare LAB 9
# Ex 2 a
def ExtrapolareRichardson(phi,x,h,n):
    PHI=np.zeros((n,n))
    for i in range(n):
        PHI[i,0]=phi(x,h/2**i)
    for i in range(1,n):
        for j in range(1,i+1):
            PHI[i,j]=1/(2**j-1)*(2**j*PHI[i,j-1]-PHI[i-1,j-1])
            
    return PHI[n-1,n-1]

#%%
f=lambda x: np.exp(2*x)
df=lambda x: 2*np.exp(2*x)

phi_1=lambda x,h: (f(x+h)-f(x))/h # aprox cu dif fin asc
phi_1=lambda x,h: (f(x)-f(x-h))/h # aprox cu dif fin desc

x=0
h=0.1

print(df(x))
print(phi_1(x,h))

n=3
dfhn=ExtrapolareRichardson(phi_1,x,h,n)
print(dfhn)

#%% LAB 10
# Ex 1 a
def CuadDreptunghi(f,a,b):
    return f((a+b)/2)*(b-a)

def CuadTrapez(f,a,b):
    return (f(a)+f(b))*(b-a)/2

def CuadSimpson(f,a,b):
    return (f(a)+4*f((a+b)/2)+f(b))*(b-a)/6

def CuadNewton(f,a,b):
    return (f(a)+3*f((2*a+b)/3)+3*f((a+2*b)/3)+f(b))*(b-a)/8

#%%
f=lambda x: np.exp(-x**2)
a=0
b=1

I_dr=CuadDreptunghi(f,a,b)
I_tr=CuadTrapez(f,a,b)
I_S=CuadSimpson(f,a,b)
I_N=CuadNewton(f,a,b)

I_py=integrate.quad(f,a,b)[0] # obtinuta cu python

print('D:',I_dr)
print('T:',I_tr)
print('S:',I_S)
print('N:',I_N)
print('P:',I_py)

#%% fill area
xd=np.linspace(a,b,100)
fig=plt.figure()
ax=fig.gca()
ax.plot(xd,f(xd))
ax.fill_between(xd,f(xd),alpha=0.5)

# dreptunghi
ax.fill_between([a,(a+b)/2,b],[f((a+b)/2)],alpha=0.3)

# trapez
ax.fill_between([a,b],[f(a),f(b)],alpha=0.3)