import scipy.integrate as integrate

def GramSchmidt(w, a, b, n):

    phi0 = lambda x: 1+0*x
    
    a1 = integrate.quad(lambda x: w(x) * x * phi0(x)**2, a, b)[0] / integrate.quad(lambda x: w(x) * phi0(x)**2, a, b)[0]
    phi1 = lambda x: x - a1
    PHI=[phi0, phi1]
    for k in range(2, n+1):
   
        ak = integrate.quad(lambda x: w(x) * x * PHI[k - 1](x)**2, a, b)[0] / integrate.quad(lambda x: w(x) * PHI[k-1](x)**2, a, b)[0]
        bk = integrate.quad(lambda x: w(x) * x * PHI[k - 1](x) * PHI[k - 2](x), a, b)[0] / integrate.quad(lambda x: w(x) * PHI[k - 2](x)**2, a, b)[0]

        phik = lambda x: (x - ak) * PHI[k - 1](x) - bk * PHI[k - 2](x)
        PHI.append(phik)
   
    return PHI