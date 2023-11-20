# -*- coding: utf-8 -*-
import numpy as np

# define the coefficient matrix A
A = np.array([[2, 4], 
             [6, 8]])

# define the constant vector b
b = np.array([5, 6])

# solve the system of linear equations Ax = b
x = np.linalg.solve(A, b)

print(x)

# Output: [-2.  2.25]
