import numpy as np
import matplotlib.pyplot as plt
from Ex1a import FDM

def f(x): return np.exp(2*x)
def fd(x): return 2*np.exp(2*x)

x = 0
#b1)
modes = ['ascendent', 'descendent', 'centrat']
for i in range(3):
    print(modes[i])
    print("%s %s %s %s" % ("h           ", "df          ", "aprox       ", "errAbs")) 
    for k in range (1,11):
        h = 1/k
        aprox, errAbs=FDM(f,fd,x,h)
        print("%.10f %.10f %.10f %.4e" % (h, fd(x), aprox[i], errAbs[i]))

#b2)
list1 = []
list2 = []
list3 = []
for k in range (1,11):
    h = 1/k
    aprox, errAbs=FDM(f,fd,x,h)
    list1.append(h)
    list2.append(errAbs[2])
    list3.append(h**2)

   
plt.loglog(list1, list2)
plt.loglog(list1, list3)

plt.show()
