import numpy as np 
dx = 0.1; y = [1, 2, 3, 4, 4, 5, 6] # dx constant
arr= np.gradient(y, dx) # dy/dx 2nd order accurate

print(arr)

