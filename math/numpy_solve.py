# -*- coding: utf-8 -*-
''' Solve a system of equations using numpy.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2023, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

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
