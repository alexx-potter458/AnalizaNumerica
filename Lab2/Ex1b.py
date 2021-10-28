import matplotlib.pyplot as plt
import numpy as np
from Ex1a import metPunctFix
from Ex1a import metPunctFixAndPrint

rangeX = np.linspace(1,2)

def phi1(x): return -x**3 - 4*(x**2) + 10 + x
y1 = phi1(rangeX);

def phiD1(x): return abs((-3*(x**2)) - (8*x) + 1)
y1d = phiD1(rangeX)

def phi2(x): return np.sqrt((10/x) - 4*x)
y2 = phi2(rangeX)

def phiD2(x): return abs((-(10/(x**2)) - 4) / 2*np.sqrt((10/x) - 4*x))
y2d = phiD2(rangeX)

def phi3(x): return (1/2) * np.sqrt(10 - x**3)
y3 = phi3(rangeX)

def phiD3(x): return abs(-((3*x**2) / 4*np.sqrt(10 - x**3)))
y3d = phiD3(rangeX)

def phi4(x): return np.sqrt(10/(x+4))
y4 = phi4(rangeX)

def phiD4(x): return abs(- (np.sqrt(10) / 2*(x + 4)**(3/2)))
y4d = phiD4(rangeX)

# #b1
# def f(x): return x**3 + 4*(x**2) - 10
# Y = f(rangeX);
# plt.plot(rangeX, Y, color="black")

# # b2i
# plt.plot(rangeX, y1, color="gray")
# plt.plot(rangeX, y1d, color="blue")

# #b2ii
# plt.plot(rangeX, y2, color="green")
# plt.plot(rangeX, y2d, color="blue")
# # graficele se suprapun

# #b2iii
# plt.plot(rangeX, y3, color="gray")
# plt.plot(rangeX, y3d, color="blue")

# #b2iv
# plt.plot(rangeX, y4, color="red")
# plt.plot(rangeX, y4d, color="pink")

# #b3
# x1n = metPunctFix(phi1, 1, 20)
# print("1. ", x1n)

# x2n = metPunctFix(phi2, 1, 20)
# print("2. ", x2n)

# x3n = metPunctFix(phi3, 1, 20)
# print("3. ", x3n)

# x4n = metPunctFix(phi4, 1, 20)
# print("4. ", x4n)

#b4
#phi4 e mai rapid decat phi deoarece se apropie mai repede de 1.36 in iteratii
print()
x3n = metPunctFixAndPrint(phi3, 1, 20)
print("3. ", x3n)
print()
x4n = metPunctFixAndPrint(phi4, 1, 20)
print("4. ", x4n)

plt.axhline(0)
plt.show()