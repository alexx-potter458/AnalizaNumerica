# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 11:53:46 2021

@author: Andreea Grecu
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#%% Ex 1 a-b
def MetBaricentrica(f,a,b,n,x):
    # noduri echidistante
    xd=np.linspace(a,b,n+1)
    # sau noduri Chebyshev, pentru a diminua fenomenul Runge
    for k in range(n+1):
        xd[k]=(a+b)/2+(b-a)/2*np.cos(k*np.pi/n)
    yd=f(xd)
    w=np.ones(n+1)
    p=1
    y=0
    for k in range(n+1):
        for i in range(n+1):
            if i!=k:
                w[k]=w[k]/(xd[k]-xd[i])
        p=p*(x-xd[k])
        y=y+(w[k]*yd[k])/(x-xd[k])    
    y=y*p
    return y

#%%
f=lambda x: np.exp(2*x)
f=lambda x: 1/(1+12*x**2)
a=-1
b=1
n=3

x=0.5
y=MetBaricentrica(f,a,b,n,x)
print(y)
print(f(x))

#%% 
xdd=np.linspace(a,b,100)
plt.figure()
plt.plot(xdd,f(xdd),label='$f(x)$')

MetBaricentrica_vec=np.vectorize(MetBaricentrica)

for n in range(1,10):
    yB=MetBaricentrica_vec(f,a,b,n,xdd)
    plt.pause(2)
    plt.cla()
    plt.plot(xdd,f(xdd),'--',label='$f(x)$')
    plt.plot(xdd,yB,label='polinomul de interp P'+str(n))
    plt.legend()

#%%
plt.figure()
for n in range(1,5):
    yB=MetBaricentrica_vec(f,a,b,n,xdd)
    err_abs=abs(f(xdd)-yB)
    plt.pause(1)
    plt.plot(xdd,err_abs,label=str(n))
    plt.title('Graficul erorii absolute')
    plt.legend()
    
#%% Ex 2 a
def MetHermite_sym(f,df,a,b,n,x):
    xd=np.linspace(a,b,n+1)
    yd=f(xd)
    dyd=df(xd)
    t=sym.symbols('t')
    P=0*t
    for k in range(n+1):
        L=1+0*t
        for i in range(n+1):
            if i!=k:
                L=L*(t-xd[i])/(xd[k]-xd[i])
        dL=sym.diff(L)
        H=L**2*(1-2*dL.subs(t,xd[k])*(t-xd[k]))
        K=L**2*(t-xd[k])
        P=P+yd[k]*H+dyd[k]*K
    y=P.subs(t,x)
    return y, P

#%%
f=lambda x: np.exp(2*x)
df=lambda x: 2*np.exp(2*x)
a=-1
b=1
n=3

x=0.5
y,P_sym=MetHermite_sym(f,df,a,b,n,x)

print(y)
print(f(x))

#%% 2 c
xdd=np.linspace(a,b,100)
plt.figure()
plt.plot(xdd,f(xdd),label='$e^{2x}$')

for n in range(1,4):
    y,P_sym=MetHermite_sym(f,df,a,b,n,x)
    t=sym.symbols('t')
    P=sym.lambdify(t,P_sym)
    
    plt.pause(1)
    plt.plot(xdd,P(xdd),label='polinomul de interp P'+str(2*n+1))
    plt.legend()

#%% 
plt.figure()
for n in range(1,4):
    y,P_sym=MetHermite_sym(f,df,a,b,n,x)
    t=sym.symbols('t')
    P=sym.lambdify(t,P_sym)
    
    err_abs=lambda t: abs(f(t)-P(t))
    
    plt.pause(1)
    plt.plot(xdd,err_abs(xdd),label=str(2*n+1))
    plt.title('Graficul erorii absolute')
    plt.legend()
    
#%% Ex 2 b
def MetHermiteDD(f,df,a,b,n,x):
    xd=np.linspace(a,b,n+1)
    yd=f(xd)
    dyd=df(xd)
    z=np.zeros(2*n+2)
    z[0:2*n+2:2]=xd
    z[1:2*n+2:2]=xd
    DD=np.zeros((2*n+2,2*n+2))
    DD[:,0]=f(z)
    DD[1:2*n+2:2,1]=dyd
    for i in range(2,2*n+2,2):
        DD[i][1]=(DD[i][1-1]-DD[i-1][1-1])/(z[i]-z[i-1])    
    for i in range(2,2*n+2):
        for j in range(2,i+1):
            DD[i][j]=(DD[i][j-1]-DD[i-1][j-1])/(z[i]-z[i-j])
    y=DD[0,0]
    produs=1
    for k in range(1,2*n+2):
        produs=produs*(x-z[k-1])
        y=y+DD[k][k]*produs
    return y

#%% 
f=lambda x: np.exp(2*x)
df=lambda x: 2*np.exp(2*x)
a=-1
b=1
n=3

x=0.5
y=MetHermiteDD(f,df,a,b,n,x)
print(y)
print(f(x))

#%% 2 c
xdd=np.linspace(a,b,100)
plt.figure()
plt.plot(xdd,f(xdd),label='$e^{2x}$')

MetHermiteDD_vec=np.vectorize(MetHermiteDD)

for n in range(1,4):
    yHDD=MetHermiteDD_vec(f,df,a,b,n,xdd)
    plt.pause(1)
    plt.plot(xdd,yHDD,label='polinomul de interp P'+str(2*n+1))
    plt.legend()

#%%
plt.figure()
for n in range(1,4):
    yHDD=MetHermiteDD_vec(f,df,a,b,n,xdd)
    err_abs=abs(f(xdd)-yHDD)
    plt.pause(3)
    plt.plot(xdd,err_abs,label=str(2*n+1))
    plt.title('Graficul erorii absolute')
    plt.legend()