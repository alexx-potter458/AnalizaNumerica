def Secantaf(f, a, b, itmax):
    xOld = a
    xn = b

    print("Secantaf starting:")

    for i in range(itmax):
        aux = xn
        if f(xn) == f(xOld):
            print('Here explodes 0/0!')
            break
        xn = xn - f(xn)*((xn-xOld) / (f(xn)-f(xOld)))
        xOld = aux
        print("%d. xn=%.10f --  errRel=%.4e" % (i+1, xn, abs((xn-xOld)/xOld)))


def PozitieFalsaf(f, a, b, itmax):
    xOldest = a
    xOld = b
    xn = b - f(a)*((b-a) / (f(b)-f(a)))
    
    print("PozitieFalsaf starting:")

    for i in range(itmax):
        aux = xn
        aux2 = xOld
        if xn*xOld <= 0:
            if f(xn) == f(xOld):
                print('Here explodes 0/0!')
                break
            xn =xn - f(xn)*((xn-xOld) / (f(xn)-f(xOld)))
        else:
            if f(xn) == f(xOldest):
                print('Here explodes 0/0!')
                break
            xn =xn - f(xn)*((xn-xOldest) / (f(xn)-f(xOldest)))

        print("%d. xn=%.10f --  errRel=%.4e" % (i+1, xn, abs((xn-xOld)/xOld)))
        
        xOld = aux
        xOldest = aux2