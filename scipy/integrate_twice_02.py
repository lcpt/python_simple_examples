
import numpy as np
from scipy.integrate import trapz

def a(x):
    return x

def samplePoints(x0, x1, n):
    ''' Return a list of sample points.

    :param x0: interval beginning.
    :param x1: interval end.
    :param n: number of divisions.
    '''
    xi= x0; step= (x1-x0)/n
    retval= list()
    for i in range(0, n+1):
        retval.append(xi)
        xi+= step
    return np.array(retval)

def sampleOrdinates(xi):
    ''' Return sample ordinates.

    :param xi: abcissae.
    '''
    retval= list()
    for x in xi:
        retval.append(a(x))
    return retval

def firstIntegral(lb, ub, a, n):
    ''' Compute the first integral from the sample points.

    :param lb: lower bound.
    :parma ub: upper bound.
    :param a: function to integrate.
    '''
    yi= list()
    xi= samplePoints(lb, ub, n)
    for x in xi:
        yi.append(a(x))    
    return trapz(yi, xi)

def secondIntegral(lb, ub, a, n):
    ''' Compute the first integral from the sample points.

    :param lb: lower bound.
    :parma ub: upper bound.
    :param a: function to integrate.
    '''
    xi= samplePoints(lb, ub, n)    
    increments= [0.0]
    xA= xi[0]
    for x in xi[1:]:
        increment= firstIntegral(xA, x, a, n)
        increments.append(increment)
        xA= x
    first_integral= (np.add.accumulate(increments))
    return trapz(first_integral, xi)

lb, ub = 0.0, 1.0
n= 10

integral1 = firstIntegral(lb, ub, a, n)
error1= abs(integral1-1/2.0)/(1/2.0)
integral2 = secondIntegral(lb, ub, a, n)
error2= abs(integral2-1/6.0)/(1/6.0)
print('integral1: ', integral1, 'error1= ', error1)
print('integral2: ', integral2, 'error2= ', error2)

