
import math
import numpy as np

def getIntervalCenters(n):
    ''' Get the centers of the intervals in natural coordinates.

    :param n: number of intervals.
    '''
    sz= 2.0/n
    xi= np.linspace(start= -1, stop= 1, num= n+1, endpoint= True)
    return [ x+sz/2.0 for x in xi[:-1]] # Centers of the intervals.
    
avgWidth= 2.0
eSize= 0.5
nDivWidth= int(math.ceil(avgWidth/eSize))

xi= getIntervalCenters(nDivWidth)

print(nDivWidth, eSize)
print(xi)
