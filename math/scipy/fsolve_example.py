''' x0*cos(x1) = 4,  x1*x0 - x1 = 5.'''

import numpy as np

from scipy.optimize import fsolve

def func(x):

    return [x[0] * np.cos(x[1]) - 4,

            x[1] * x[0] - x[1] - 5]

root = fsolve(func, [1, 1])

print(root)

print(np.isclose(func(root), [0.0, 0.0]))
