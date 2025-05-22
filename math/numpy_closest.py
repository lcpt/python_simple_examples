# Python3 program to find Closest number in a list
import numpy as np
def closest(lst, K):
    
     lst = np.asarray(lst)
     idx = (np.abs(lst - K)).argmin()
     return lst[idx]
    
# Driver code
lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
K = 9.1
print(closest(lst, K))
