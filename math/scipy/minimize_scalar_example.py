''' Minimize scalar small example.'''
from scipy import optimize

def fun(s,t):
    return (s-t)*s*(s+t)**3

optimize.show_options(solver='minimize_scalar', method='bounded', disp=True)

result= optimize.minimize_scalar(fun, args= (3))
print(result.x)
print(result.nfev)

