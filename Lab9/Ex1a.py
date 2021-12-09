import numpy as np

def FDM(f,df,x,h):
    dfa=(f(x+h)-f(x))/h
    dfd=(f(x)-f(x-h))/h
    dfc=(f(x+h)-f(x-h))/(2*h)
    
    aprox=np.array([dfa,dfd,dfc])
    
    errAbs=abs(df(x)-aprox)
    
    return aprox, errAbs