import numpy as np

def CuadGauss(f,a,b): # pentru n=1
    x=np.array([(a+b)/2-(b-a)/2*np.sqrt(3)/3,(a+b)/2+(b-a)/2*np.sqrt(3)/3])
    w=np.array([(b-a)/2,(b-a)/2])
    I=0
    for i in range(2):
        I=I+f(x[i])*w[i]
    return I