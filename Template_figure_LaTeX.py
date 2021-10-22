import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt


# ==============================================================
# Template formatare figura
# ==============================================================
f = lambda x: x + np.exp(- x ** 2) * np.cos(x)
               
# Formatare text figura
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
              "size": 14,
             }

# Discretizare interval
a, b = -1, 1
x = np.linspace(a,b)

# Creare figura
plt.figure()
plt.title("Solutia ecuatiei $x + e^{-x^2}\cos(x) = 0$", fontdict = TitleFont)
plt.style.use('seaborn-ticks')
plt.grid(color='grey', linestyle='-', linewidth=0.5)
plt.xlabel("x", fontdict = AxisFont)
plt.ylabel("y", fontdict = AxisFont)
plt.plot(x, f(x), \
         linestyle = "-", linewidth = 2.0, color = "blue")
plt.axhline(0, c='red', linestyle = "--", linewidth=2.0)
plt.legend(["$f(x) = x + e^{-x^2}\cos(x)$", "$y = 0$"], 
           prop = LegendProp, loc = "lower center")
    
# Salveaza figura
filename = "Graficf.eps"
plt.savefig(filename)