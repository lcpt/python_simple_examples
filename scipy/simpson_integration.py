import numpy as np
import scipy.integrate

def f1(x):

   return x**2


x = np.array([1,3,4])

y1 = f1(x)



I1 = scipy.integrate.simps(y1, x)
ok= (I1==21)

print('I1= ', I1, 'OK: ', ok)

