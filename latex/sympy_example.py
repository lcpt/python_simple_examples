# -*- coding: utf-8 -*-

import sympy

expr= '(-b-sqrt(b**2-4*a*c))/(2*a)'
ltxString= sympy.latex(sympy.sympify(expr))

print(ltxString)
