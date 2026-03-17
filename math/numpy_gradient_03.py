import numpy as np
from matplotlib import pyplot as plt

# we sample a sin(x) function
dx = np.pi/10
x = np.arange(0,2*np.pi,np.pi/10)

# we calculate the derivative, with np.gradient
plt.plot(x,np.gradient(np.sin(x), dx), '-*', label='approx')

# we compare it with the exact first derivative, i.e. cos(x)
plt.plot(x,np.cos(x), label='exact')
plt.legend()
plt.show()
