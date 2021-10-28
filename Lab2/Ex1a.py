import matplotlib.pyplot as plt
import numpy as np

def metPunctFix(phi, xn, n):
    for i in range(n):
        if xn > 1000000000000000:
            return "This one exploded"
        xn = phi(xn)
    return xn

def metPunctFixAndPrint(phi, xn, n):
    for i in range(n):
        if xn > 1000000000000000:
            return "This one exploded"
        xn = phi(xn)
        print(i, " = ", xn)
    return xn