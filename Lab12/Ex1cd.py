import numpy as np
import matplotlib.pyplot as plt
from Ex1a import GramSchmidt
from Ex1b import AproxL2

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