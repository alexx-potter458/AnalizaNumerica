import scipy.integrate as integrate
import numpy as np
from Ex1a import GramSchmidt

def AproxL2(f,w,a,b,n):
    PHI = GramSchmidt(w, a, b, n)
    c = np.zeros(n + 1)
    for i in range(n + 1):
        c[i] = integrate.quad(lambda x: w(x) * PHI[i](x) * f(x), a, b)[0] / integrate.quad(lambda x: w(x) * PHI[i](x)**2, a, b)[0]
    return c
