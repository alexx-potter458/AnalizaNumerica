"""
Titlu: Elemente de calcul stiintific, Laboratorul #3

Autor: Mihai Bucataru, Februarie 2021.
#==============================================================================
"""
# Importam toate librariile si functiile necesare exercitiilor din laborator
import numpy as np
import matplotlib.pyplot as plt
from math import factorial


"""
Obs: Adauga/elimina termeni pentru a vizualiza convergenta aproximarii
functiei exponentiale cu polinomul Taylor asociat.
"""


# Aproximare polinom Taylor
def polinom_Taylor(x):
    """"Polinomul de aproximare Taylor a functiei exp(2 * x)"""
    return 1 + 2 * x / factorial(1) \
             #+ (2 * x)**2 / factorial(2) \
             #+ (2 * x)**3 / factorial(3) \
             #+ (2 * x)**4 / factorial(4) \
             #+ (2 * x)**5 / factorial(5)


# Pasul aproximarii
h = .001

# Formateaza scrisul pentru axe, titlu si legenda
AxisFont = {"family": "arial",
            "color":  "black",
            "weight": "normal",
            "size": 16,
           }
TitleFont = {"family": "serif",
             "color":  "black",
             "weight": "normal",
             "size": 16,
            }
LegendProp = {"family": "times new roman",
              "weight": "normal",
              "size": 12,
             }

# Figura aproximarea cu serii Taylor
x = np.linspace(-h, h, 100) # Discretizare a intervalului
plt.figure(0)
plt.plot(x, np.exp(2 * x), linestyle = '-', c = 'black', linewidth = 3)
plt.plot(x, polinom_Taylor(x), linestyle = '--', c = 'red', linewidth = 3)
plt.grid(color='grey', linestyle='-', linewidth=0.5)
plt.legend(['$e^{2x}$', 'Polinom Taylor'], prop = LegendProp)  # Adauga legenda
# plt.axvline(0, c='black')  # Adauga axa OY
# plt.axhline(0, c='black')  # Adauga axa OX
plt.axis("tight")
plt.xlabel('x', fontdict = AxisFont)  # Label pentru axa OX
plt.ylabel('y', fontdict = AxisFont)  # Label pentru axa OY
plt.title('Aproximarea unei functii cu polionmul Taylor', fontdict = TitleFont)
plt.show()  # Arata graficul
