import numpy as np

def SplineLiniar(f,a,b,n,x):

    xDivs = np.linspace(a,b,n+1)
    yDivs=f(xDivs)

    for j in range(n):
        if xDivs[j] <= x <= xDivs[j+1]:
            
            a = yDivs[j]
            b = (yDivs[j+1] - yDivs[j]) / (xDivs[j+1] - xDivs[j])
            
            y = a + b * (x - xDivs[j])
            return y
     