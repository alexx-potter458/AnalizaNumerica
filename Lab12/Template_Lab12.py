import numpy as np
import matplotlib.pyplot as plt


def Int_num(f, a, b, m=100):
    """
    Integrarea numerica sumata a functiei f pe intervalul [a,b] folosind 
    metoda dreptunchiului si m subdiviziuni egale. O vom folosi 
    pentru calculul produselor scalare ponderate.

    Parameters
    ----------
    f : FUNCTION.
        FUNCTION TO BE NUMERICALLY INTEGRATED.
    a : FLOAT
        LEFT ENDPOINT.
    b : FLOAT
        RIGHT ENDPOINT.
    m : INTEGER
        NO. OF INTERVAL SUBDIVISIONS.

    Returns
    -------
    I_num : FLOAT
            NUMERICAL INTEGRAL
    """
    
    
    x = np.linspace(a, b, m + 1)  # m subdiviziuni
    
    I_num = 0
    for i in range(m):
        I_num += (x[i+1] - x[i]) * f((x[i] + x[i+1]) / 2)  # Dreptunghiuri
    
    return I_num


def GramSchmidt(a, b, w, n):
    """
    Construcita unei baze ortogonale in P_n(a,b) folosind Gram-Schmidt in
    raport cu produsul scalar ponderat cu w(x). Vom reprezenta cele n + 1
    polinoame obtinute folosind o matrice C, ce va contine pe fiecare linie
    coeficientii celor n + 1 polinoame ortogonale. Mai exact, pe prima coloana
    avem coeficientul dominant si pe diagonala coeficientul termenului liber.
    
    Parameters
    ----------
    a : FLOAT
        LEFT ENDPOINT.
    b : FLOAT
        RIGHT ENDPOINT.
    w : FUNCTION.
        WEIGHT FUNCTION THAT DEFINES THE WEIGHTED SCALAR PRODUCT.
    n : INTEGER
        POLYNOMIAL SPACE DIMENSION - 1.

    Returns
    -------
    C : FLOAT LOWER TRIANGULAR MATRIX OF SIZE n + 1
        EACH LINE CONTAINS THE COEFFICIENTS OF EACH ORTHOGONAL POLYNOMIAL, 
        ORDERED FROM THE LEADING COEFFICIENT TO THE FREE COEFICIENT.
    """
    
    
    C = np.zeros((n + 1, n + 1))
    
    # phi_0 = 1
    # ...
    
    # phi_1 = (x - A) * phi_0 = x - A
    # ...
    
    # phi_k = (x - A) * phi_{k-1} - B * phi_{k-2}
    # ...

    return C


def AproximareL2(f, a, b, w, n):
    """
    Aproximarea functiei f in spatiul P_n(a,b) folosind norma indusa de 
    produsul scalar ponderat de w, calculata optim, i.e. folosind o baza
    ortogonala a spatiului polinomial P_n(a,b) generata de metoda Gram-Schmidt.

    Parameters
    ----------
    f : FUNCTION.
        FUNCTION TO BE APPROXIMATED.
    a : FLOAT
        LEFT ENDPOINT.
    b : FLOAT
        RIGHT ENDPOINT.
    w : FUNCTION.
        WEIGHT FUNCTION THAT DEFINES THE WEIGHTED SCALAR PRODUCT.
    n : INTEGER
        POLYNOMIAL SPACE DIMENSION - 1.

    Returns
    -------
    c : FLOAT COLUMN ARRAY OF SIZE n + 1
        THE n + 1 COEFFICIENTS OF THE L2-APPROXIMATION POLYNOMIAL
    """
    
    
    # Construieste baza ortogonala de polinoame folosind Gram-Schmidt
    C = GramSchmidt(a, b, w, n)  # (Poate fi introdusa si ca parametru intrare)
    
    # Proiectia L2
    c = np.zeros(n+1)
    # ...
                  
    return c
    
            
# ==============================================================
# Exercitiul #1
# ==============================================================
# Datele problemei pentru subpunctul (c)
f = lambda x: x ** 2 - 2 * x + 3
a, b = -1, 1
x_grafic = np.linspace(a, b)
w = lambda x: 1
NMAX = 0

# Rezolvare
for n in range(NMAX + 1):
    # Initializare grafic
    plt.figure()
    plt.title("Aproximarea $L^2$ in $P_{%d}$" %n)
    plt.style.use('seaborn-ticks')
    plt.grid(color='grey', linestyle='-', linewidth=0.5)
    plt.xlabel("x")
    plt.ylabel("y")
    
    # Aplica Gram-Schmidt pentru a construi o baza ortogonala de polinoame
    C = GramSchmidt(a, b, w, n)
    with np.printoptions(precision=3, suppress=True):
        print(C)
    
    # Determina coeficientii celei mai bune aproximari polinomiale in aceasta baza
    Coef_L2 = AproximareL2(f, a, b, w, n) 
    
    # Evaluam polinomul de aproximare obtinut in fiecare nod de reprezentare
    Pn_L2 = np.zeros(len(x_grafic))
    for i in range(len(x_grafic)):
        for j in range(n + 1):  
            # Evaluam intai polinom orgotonal phi_j in nodul de reprezentare
            phi_j = C[j,:j+1] @ np.power(x_grafic[i] * np.ones(j+1), np.arange(j,-1,-1))
            # Adaugam polinomul ortogonal inmultit cu coeficientul corespunzator
            Pn_L2[i] += Coef_L2[j] * phi_j
                
    # Graficul celei mai bune aproximari polinomiale
    plt.plot(x_grafic, f(x_grafic), linewidth = 2, color = "blue")
    plt.plot(x_grafic, Pn_L2, c = 'red', linestyle = '--', linewidth = 2)
    
    # Graficul erorii absolute a aproximarii
    # ...
