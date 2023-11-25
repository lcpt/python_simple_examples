from scipy import optimize

def f(x):

   return (x**3 - 1)  # only one real root at x = 1


sol = optimize.root_scalar(f, bracket=[0, 3], method='brentq')

#print('Brentq method',sol)
print(sol.root)
sol = optimize.root_scalar(f, bracket=[0, 3], method='bisect')
#print('Bisect method',sol)

print(sol.root)
