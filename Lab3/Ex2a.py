def Secantaf(f, a, b, tol):
    solution = [a,b]
    xOld = a
    xn = b
    i = 0
    print("Secantaf starting:")

    while abs(f(xn)) >= tol:
        aux = xn
        if f(xn) == f(xOld):
            print('Here explodes 0/0!')
            break
        xn = xn - f(xn)*((xn-xOld) / (f(xn)-f(xOld)))
        solution.append(xn)
        xOld = aux
        print("%d. xn=%.10f --  errRel=%.4e" % (i+1, xn, abs((xn-xOld)/xOld)))
        i+=1

    return solution

def PozitieFalsaf(f, a, b, tol):
    solution = [a,b]
    xOldest = a
    xOld = b
    xn = b - f(a)*((b-a) / (f(b)-f(a)))
    i = 0
    print("PozitieFalsaf starting:")

    while abs(f(xn)) >= tol:
        aux = xn
        aux2 = xOld
        if xn*xOld <= 0:
            if f(xn) == f(xOld):
                print('Here explodes 0/0!')
                break
            xn = xn - f(xn)*((xn-xOld) / (f(xn)-f(xOld)))
        else:
            if f(xn) == f(xOldest):
                print('Here explodes 0/0!')
                break
            xn = xn - f(xn)*((xn-xOldest) / (f(xn)-f(xOldest)))
            
        solution.append(xn)
        print("%d. xn=%.10f --  errRel=%.4e" % (i+1, xn, abs((xn-xOld)/xOld)))
        
        xOld = aux
        xOldest = aux2
        i+=1
        
        return solution