import numpy as np
import matplotlib.pyplot as plt
from Ex2a import MetHermite
from Ex2b import MetHermiteDD

def f(x): return np.exp(2*x)
def fd(x): return 2*np.exp(2*x)
a = -1
b = 1
n = [1, 2, 3]
x = np.linspace(a, b)
 
#c1
PnMH = []
PnMHDD = []

for ni in n:
    pnMH = []
    pnMHDD = []

    for xi in x:
        pnMH.append(MetHermite(f, fd, a, b, ni, xi))
        pnMHDD.append(MetHermiteDD(f, fd, a, b, ni, xi))
    PnMH.append(pnMH)
    PnMHDD.append(pnMHDD)

#c2
for i in range(len(PnMH)):
    plt.figure()
    plt.title('Graficul pentru n=' + str(n[i]))
    plt.plot(x, f(x))
    plt.plot(x, PnMH[i], linestyle="--")
    plt.scatter(x, PnMHDD[i], marker="<")

plt.show()

#c3
def errAbs(y, yp): return abs(y-yp)
for i in range(len(PnMH)):
    plt.figure()
    plt.title('Graficul erorii pentru n=' + str(n[i]))
    errs = errAbs(f(x),  PnMHDD[i])
    plt.plot(x, errs)

plt.show()

#sau
def errAbs(y, yp): return abs(y-yp)
plt.figure()
plt.title('Graficul erorii')

for i in range(len(PnMH)):
    errs = errAbs(f(x),  PnMHDD[i])
    plt.plot(x, errs)


plt.show()
