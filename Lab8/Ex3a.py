import numpy as np

def SplineCubic(f,a,b,n,x):

    xDivs = np.linspace(a,b,n+1)
    yDivs=f(xDivs)
    n = n+1

    xdiff = np.diff(xDivs)
    ydiff = np.diff(yDivs)

    Li = np.zeros(n)
    Li_1 = np.zeros(n-1)
    zDivs = np.zeros(n)

    Li[0] = xdiff[0]**(1/2)
    Li_1[0] = 0
    zDivs[0] = 0

    for i in range(1, n-1, 1):
        Li_1[i] = xdiff[i-1] / Li[i-1]
        Li[i] = (2 * (xdiff[i - 1] + xdiff[i]) - Li_1[i - 1] * Li_1[i - 1])**(1/2)
        
        Bi = 6 * (ydiff[i] / xdiff[i] - ydiff[i - 1] / xdiff[i - 1])
        zDivs[i] = (Bi - Li_1[i - 1] * zDivs[i - 1]) / Li[i]

    i = n - 1
    
    Li_1[i - 1] = xdiff[-1] / Li[i - 1]
    Li[i] = (2 * xdiff[-1] - Li_1[i - 1] * Li_1[i - 1])**(1/2)
    
    Bi = 0
    
    zDivs[i] = (Bi - Li_1[i - 1] * zDivs[i - 1]) / Li[i]

    i = n - 1
    zDivs[i] = zDivs[i] / Li[i]
    
    for i in range(n-2, -1, -1):
        zDivs[i] = (zDivs[i] - Li_1[i - 1] * zDivs[i + 1]) / Li[i]

    i = xDivs.searchsorted(x)

    xi1, xi0 = xDivs[i], xDivs[i - 1]
    yi1, yi0 = yDivs[i], yDivs[i - 1]
    zi1, zi0 = zDivs[i], zDivs[i - 1]
    hi1 = xi1 - xi0

    y = zi0 / (6 * hi1) * (xi1 - x)**3 + zi1 / (6 * hi1)*(x - xi0)**3 + (yi1 / hi1 - zi1 * hi1 / 6) * (x - xi0) + (yi0 / hi1 - zi0 * hi1 / 6) * (xi1 - x)
    
    return y
