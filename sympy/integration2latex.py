from sympy import symbols
from sympy import integrate
from sympy import latex

x = symbols ( 'x ')
calcIntegrate=integrate ( " (1+ x ) **(1/2) " ,x ) 
result=integrate ( " (1+ x ) **(1/2) " ,x )
reusl2latex=latex(result)
