# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 11:50:34 2021

@author: Andreea Grecu
"""
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#%% continuare LAB 10
# Ex 2 a
def CuadSumDreptunghi(f,a,b,m):
    x=np.linspace(a,b,m+1)
    I=0
    for i in range (m):
        I=I+f((x[i]+x[i+1])/2)*(x[i+1]-x[i])
    return I, x

def CuadSumTrapez(f,a,b,m):
    x=np.linspace(a,b,m+1)
    I=0
    for i in range (m):
        I=I+(f(x[i])+f(x[i+1]))*(x[i+1]-x[i])/2
    return I, x

def CuadSumSimpson(f,a,b,m):
    x=np.linspace(a,b,m+1)
    I=0
    for i in range (m):
        I=I+(f(x[i])+4*f((x[i]+x[i+1])/2)+f(x[i+1]))*(x[i+1]-x[i])/6
    return I

def CuadSumNewton(f,a,b,m):
    x=np.linspace(a,b,m+1)
    I=0
    for i in range (m):
        I=I+(f(x[i])+3*f((2*x[i]+x[i+1])/3)+3*f((x[i]+2*x[i+1])/3)+f(x[i+1]))*(x[i+1]-x[i])/8    
    return I

#%%
f=lambda x: np.exp(-x**2)
a=0
b=1
m=5

I_dr,x_dr=CuadSumDreptunghi(f,a,b,m)
I_tr,x_tr=CuadSumTrapez(f,a,b,m)
I_S=CuadSumSimpson(f,a,b,m)
I_N=CuadSumNewton(f,a,b,m)

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

# dreptunghi sumat
for i in range(m):
    plt.pause(1)
    ax.fill_between([x_dr[i],(x_dr[i]+x_dr[i+1])/2,x_dr[i+1]],[f((x_dr[i]+x_dr[i+1])/2)],alpha=0.3)

# trapez sumat
for i in range(m):
    plt.pause(1)
    ax.fill_between([x_tr[i],x_tr[i+1]],[f(x_tr[i]),f(x_tr[i+1])],alpha=0.3)
    
#%% LAB 11
# Ex 1 a
def CuadMetCoefNedet(f,a,b,n):
    x=np.linspace(a,b,n+1)
    A=np.zeros((n+1,n+1))
    B=np.zeros(n+1)
    for i in range(n+1):
        A[i,:]=x**i
        B[i]=(b**(i+1)-a**(i+1))/(i+1)
    w=np.linalg.solve(A,B)
    I=0
    for i in range(n+1):
        I=I+f(x[i])*w[i]
    return I

#%% 1 b
def CuadGauss(f,a,b): # pentru n=1
    x=np.array([(a+b)/2-(b-a)/2*np.sqrt(3)/3,(a+b)/2+(b-a)/2*np.sqrt(3)/3])
    w=np.array([(b-a)/2,(b-a)/2])
    I=0
    for i in range(2):
        I=I+f(x[i])*w[i]
    return I

#%% 1 c
f=lambda x: np.exp(-x**2)
a=0
b=1
n=1

I_CN=CuadMetCoefNedet(f,a,b,n)
I_CG=CuadGauss(f,a,b)

I_py=integrate.quad(f,a,b)[0] # obtinuta cu python

print('CN:',I_CN)
print('CG:',I_CG)
print('Py:',I_py)

#%% Ex 2 a
def CuadHermite(f,df,a,b): # pentru n=1
    return (f(a)+f(b))*(b-a)/2+(df(a)-df(b))*(b-a)**2/12

#%% 2 b
f=lambda x: np.exp(-x**2)
df=lambda x: -2*x*np.exp(-x**2)
a=0
b=1

I_tr=(f(a)+f(b))*(b-a)/2
I_H=CuadHermite(f,df,a,b)

I_py=integrate.quad(f,a,b)[0] # obtinuta cu python

print('tr:',I_tr)
print('He:',I_H)
print('Py:',I_py)