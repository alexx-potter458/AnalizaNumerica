def Dreptunghi(f, a, b):
    return f((a + b) / 2) * (b - a)

def Trapez(f, a, b):
    return (f(a) + f(b)) * (b - a) / 2

def Simpson(f, a, b):
    return (f(a) + 4 * f((a + b) / 2) + f(b)) * (b - a) / 6

def Newton(f, a, b):
    return (f(a) + 3 * f((2 * a + b) / 3) + 3 * f((a + 2 * b) / 3) + f(b)) * (b - a) / 8