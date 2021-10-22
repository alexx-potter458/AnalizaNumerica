import matplotlib.pyplot as plt
import numpy as np
import math


def f(x): 
    power = -x**2
    return x + (math.e**power)*math.cos(x)

print("df")