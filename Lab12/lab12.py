# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:55:09 2022

@author: Andreea Grecu
"""
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

#%% Ex 1 a
def GramSchmidt(w,a,b,n):
    phi0=lambda x: 1+0*x
    a1=integrate.quad(lambda x: w(x)*x*phi0(x)**2,a,b)[0]/integrate.quad(lambda x: w(x)*phi0(x)**2,a,b)[0]
    phi1=lambda x: x-a1
    PHI=[phi0,phi1]
    for k in range(2,n+1):
        ak=integrate.quad(lambda x: w(x)*x*PHI[k-1](x)**2,a,b)[0]/integrate.quad(lambda x: w(x)*PHI[k-1](x)**2,a,b)[0]
        bk=integrate.quad(lambda x: w(x)*x*PHI[k-1](x)*PHI[k-2](x),a,b)[0]/integrate.quad(lambda x: w(x)*PHI[k-2](x)**2,a,b)[0]
        phik=lambda x: (x-ak)*PHI[k-1](x)-bk*PHI[k-2](x)
        PHI.append(phik)
    return PHI

#%% 1 b
def AproxL2(f,w,a,b,n):
    PHI=GramSchmidt(w,a,b,n)
    c=np.zeros(n+1)
    for i in range(n+1):
        c[i]=integrate.quad(lambda x: w(x)*PHI[i](x)*f(x),a,b)[0]/integrate.quad(lambda x: w(x)*PHI[i](x)**2,a,b)[0]
    return c

#%% 1 c - d
a=-1
b=1
w=lambda x: 1 + 0*x
f=lambda x: x**2-2*x+3
n=0
n=1
n=2

a=0
b=1
w=lambda x: 1 + 0*x
f=lambda x: np.exp(-x**2)
n=0
n=1
n=2

Phi=GramSchmidt(w,a,b,n)
c=AproxL2(f,w,a,b,n)

xd=np.linspace(a,b,100)
plt.figure()
plt.plot(xd,f(xd),label='f(x)')
plt.pause(1)

Pn_xd=np.zeros(100)
for i in range(n+1):
    Pn_xd=Pn_xd+c[i]*Phi[i](xd)
    
plt.plot(xd,Pn_xd,label='Polinom de grad n='+str(n))
plt.legend()

#%% Ex 2 a - b
a=-1
b=1
w=lambda x: 1 + 0*x # vom obtine pol Legendre
n=2

Phi=GramSchmidt(w,a,b,n)

xd=np.linspace(a,b,100)
plt.figure()
for i in range(n+1):
    plt.plot(xd,Phi[i](xd),label='$\phi$'+str(i))
plt.legend()

a=-1
b=1
w=lambda x: 1/np.sqrt(1-x**2) # vom obtine pol Chebyshev
n=2

Phi=GramSchmidt(w,a,b,n)

xd=np.linspace(a,b,100)
plt.figure()
for i in range(n+1):
    plt.plot(xd,Phi[i](xd),label='$\phi$'+str(i))
plt.legend()

#%% SIMBOLIC
import sympy as sym

#%% Ex 1 a
def GramSchmidt_sym(w,a,b,n):
    x=sym.symbols('x')
    phi0=1+0*x
    a1=sym.integrate(w*x*phi0**2,(x,a,b))/sym.integrate(w*phi0**2,(x,a,b))
    phi1=x-a1
    PHI=[phi0,phi1]
    for k in range(2,n+1):
        ak=sym.integrate(w*x*PHI[k-1]**2,(x,a,b))/sym.integrate(w*PHI[k-1]**2,(x,a,b))
        bk=sym.integrate(w*x*PHI[k-1]*PHI[k-2],(x,a,b))/sym.integrate(w*PHI[k-2]**2,(x,a,b))
        phik=(x-ak)*PHI[k-1]-bk*PHI[k-2]
        PHI.append(phik)
    return PHI

#%% Ex 2 a
a=-1
b=1
x=sym.symbols('x')
w=1 + 0*x # vom obtine pol Legendre
n=2

Phi=GramSchmidt_sym(w,a,b,n)
print(Phi)

#%% 2 b
a=-1
b=1
x=sym.symbols('x')
w=1/sym.sqrt(1-x**2) # vom obtine pol Chebyshev
n=2

Phi=GramSchmidt_sym(w,a,b,n)
print(Phi)