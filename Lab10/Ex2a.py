import numpy as np

def DreptunghiSumat(f, a, b, m):
    x = np.linspace(a, b, m+1)
    I = 0
    for i in range(m):
        I = I + f((x[i] + x[i+1]) / 2) * (x[i + 1] - x[i])
    return I

def TrapezSumat(f, a, b, m):
    x = np.linspace(a, b, m+1)
    I = 0
    for i in range(m):
        I = I + (f(x[i]) + f(x[i + 1])) * (x[i + 1] - x[i]) / 2
    return I

def SimpsonSumat(f, a, b, m):
    x = np.linspace(a, b, m+1)
    I = 0
    for i in range(m):
        I = I + (f(x[i]) + 4 * f((x[i] + x[i + 1]) / 2) + f(x[i + 1])) * (x[i + 1] - x[i]) / 6
    return I

def NewtonSumat(f, a, b, m):
    x = np.linspace(a, b, m + 1)
    I = 0
    for i in range(m):
        I = I + (f(x[i]) + 3 * f((2 * x[i]+ x [i + 1]) / 3) + 3 * f((x[i] + 2 * x[i + 1]) / 3) + f(x[i + 1])) * (x[i + 1] - x[i]) / 8    
    return I