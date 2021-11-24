import numpy as np

def MetBaricentrica(f,a,b,n,x):

    xDivs = np.linspace(a,b,n+1)

    for k in range(n+1):
        xDivs[k] = ((a + b) / 2) + ((b - a) / 2) * np.cos((k * np.pi) / n)

    yDivs = f(xDivs)
    y = 0
    
    wk = [1 for i in range(n+1)]
    p = 1
    
    for k in range(n+1):
        for i in range(n+1):
            if i != k:
                wk[k] = wk[k] / (xDivs[k] - xDivs[i])

        p = p * (x - xDivs[k])

        if x - xDivs[k] != 0: 
            y = y + (wk[k] * yDivs[k]) / (x - xDivs[k])    

    y = y * p

    return y