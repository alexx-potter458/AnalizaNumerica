import matplotlib.pyplot as plt
import numpy as np
import math


def bignFunction(f, a, b, itmax, tol, opt):
    
    def bisectMethod(a, b):
        interations = 0;
        numericalSolution = 0;
        x = a + (b-a)/2
        y = a
        if opt == 1:
            while abs(b-a) > tol:
                if(f(x)*f(a)) <= 0:
                    b = x
                else:
                    a = x
                x = a + (b-a)/2
                interations+=1
            numericalSolution = x

        elif opt == 2:
            while abs(x-y)/abs(y) > tol:
                if(f(x)*f(a)) <= 0:
                    b = x
                else:
                    a = x
                y = x
                x = a + (b-a)/2
                interations+=1
            numericalSolution = x

        elif opt == 3:
            while abs(f(x)) >= tol:
                if(f(x)*f(a)) <= 0:
                    b = x
                else:
                    a = x
                x = a + (b-a)/2
                interations+=1
            numericalSolution = x
        return numericalSolution, interations

    numericalSolution, interations = bisectMethod(a, b)
    return numericalSolution, interations