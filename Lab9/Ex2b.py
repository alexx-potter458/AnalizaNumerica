import numpy as np
import matplotlib.pyplot as plt
from Ex2a import Richardson

def f(x): return np.exp(2*x)
def fd(x): return 2*np.exp(2*x)

def phiAsc(x, h): return (f(x+h)-f(x))/h
def phiDesc(x, h): (f(x)-f(x-h))/h

x = 0
n = 3

print("asc")
print("%s %s %s %s" % ("h           ", "df          ", "aprox       ", "errAbs")) 

for k in range (1,11):
    h = 1 / k
    aprox = Richardson(phiAsc, x, h, n)
    print("%.10f %.10f %.10f %.4e" % (h, fd(x), aprox, abs(fd(x) - aprox)))


print("desc")
print("%s %s %s %s" % ("h           ", "df          ", "aprox       ", "errAbs")) 

for k in range (1,11):
    h = 1/k
    aprox = Richardson(phiDesc, x, h, n)
    print("%.10f %.10f %.10f %.4e" % (h, fd(x), aprox, abs(fd(x) - aprox)))