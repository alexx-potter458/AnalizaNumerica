from Ex1a import GramSchmidt
import numpy as np
import matplotlib.pyplot as plt
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
plt.show()