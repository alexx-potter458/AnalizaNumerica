# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 11:52:32 2021

@author: Andreea Grecu
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Ex 1 a
def SplineLiniar_vers0(f,a,b,n,x):
    xd=np.linspace(a,b,n+1)
    yd=f(xd)
    a=np.zeros(n)
    b=np.zeros(n)
    for j in range(n):
        a[j]=yd[j]
        b[j]=(yd[j+1]-yd[j])/(xd[j+1]-xd[j])
        if xd[j]<=x<xd[j+1]:
            y=a[j]+b[j]*(x-xd[j])
    return y

def SplineLiniar(f,a,b,n,x):
    xd=np.linspace(a,b,n+1)
    yd=f(xd)
    for j in range(n):
        if xd[j]<=x<xd[j+1]:
            a=yd[j]
            b=(yd[j+1]-yd[j])/(xd[j+1]-xd[j])
            y=a+b*(x-xd[j])
            return y
        
#%% Ex 2 a
def SplinePatratic(f,a,b,n,x,dfa):
    xd=np.linspace(a,b,n+1)
    h=xd[1]-xd[0]
    yd=f(xd)
    a=np.zeros(n)
    for j in range(n):
        a[j]=yd[j]
    M=np.zeros((2*n,2*n))
    M[0][0]=1
    t=np.zeros(2*n)
    t[0]=dfa
    for j in range(n-1):
        t[2*j+1]=yd[j+1]-yd[j]
        M[2*j+1,2*j+1]=h**2
        M[2*j+1,2*j]=h
        
        M[2*j+2,2*j+2]=-1
        M[2*j+2,2*j+1]=2*h
        M[2*j+2,2*j]=1
        
    j=n-1
    t[2*j+1]=yd[j+1]-yd[j]
    M[2*j+1,2*j+1]=h**2
    M[2*j+1,2*j]=h
        
    bc=np.linalg.solve(M,t)
    b=bc[0:2*n:2]
    c=bc[1:2*n:2]
    for j in range(n):
        if xd[j]<=x<xd[j+1]:
            y=a[j]+b[j]*(x-xd[j])+c[j]*(x-xd[j])**2
            return y
        
#%% comentariu alternativa functie anterioara
def Coef_SplinePatratic(f,a,b,n):
    xd=np.linspace(a,b,n+1)
    h=xd[1]-xd[0]
    yd=f(xd)
    a=np.zeros(n)
    for j in range(n):
        a[j]=yd[j]
    M=np.zeros((2*n,2*n))
    M[0][0]=1
    t=np.zeros(2*n)
    t[0]=dfa
    for j in range(n-1):
        t[2*j+1]=yd[j+1]-yd[j]
        M[2*j+1,2*j+1]=h**2
        M[2*j+1,2*j]=h
        
        M[2*j+2,2*j+2]=-1
        M[2*j+2,2*j+1]=2*h
        M[2*j+2,2*j]=1
        
    j=n-1
    t[2*j+1]=yd[j+1]-yd[j]
    M[2*j+1,2*j+1]=h**2
    M[2*j+1,2*j]=h
        
    bc=np.linalg.solve(M,t)
    b=bc[0:2*n:2]
    c=bc[1:2*n:2]
    
    return xd, a, b, c

def SplinePatratic2(x,xd,a,b,c):
    for j in range(n):
        if xd[j]<=x<xd[j+1]:
            y=a[j]+b[j]*(x-xd[j])+c[j]*(x-xd[j])**2
            return y

#%%
f=lambda x: np.exp(2*x)
df=lambda x: 2*np.exp(2*x)

a=-1
b=1
n=5

x=0.5
y=SplineLiniar(f,a,b,n,x)

print(y)
print(f(x))

dfa=df(a)
y=SplinePatratic(f,a,b,n,x,dfa)

print(y)
print(f(x))

#%% 1 b
xdd=np.linspace(a,b,100)

Spline_vec=np.vectorize(SplineLiniar)
yS=Spline_vec(f,a,b,n,xdd)

Spline_vec=np.vectorize(SplinePatratic)
yS=Spline_vec(f,a,b,n,xdd,dfa)

plt.figure()
plt.plot(xdd,f(xdd),'--',label='$f(x)$')
plt.plot(xdd,yS,label='Spline')
plt.legend()