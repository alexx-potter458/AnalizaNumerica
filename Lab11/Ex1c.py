import numpy as np
from Ex1a import CuadMetCoefNedet
from Ex1b import CuadGauss
f=lambda x: np.exp(-x**2)
a=0
b=1
n=1

I_CN=CuadMetCoefNedet(f,a,b,n)
I_CG=CuadGauss(f,a,b)

print('CN:',I_CN)
print('CG:',I_CG)