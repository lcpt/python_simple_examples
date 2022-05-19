import math
from scipy.integrate import quad

def a(x):
    return x

lb, ub = 0.0, 1.0

integral = quad(lambda x: quad(a, 0, x)[0], lb, ub)[0]
error= abs(integral-1/6.0)/(1/6.0)
print('integral: ', integral, 'error= ', error)

