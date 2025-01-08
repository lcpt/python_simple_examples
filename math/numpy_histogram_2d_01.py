''' Example taken from 
https://numpy.org/doc/2.1/reference/generated/numpy.histogram2d.html
'''
import numpy as np
import matplotlib.pyplot as plt

n = 10000
x = np.linspace(1, 100, n)
y = 2*np.log(x) + np.random.rand(n) - 0.5

# Compute 2d histogram. Note the order of x/y and xedges/yedges

H, yedges, xedges = np.histogram2d(y, x, bins=20)

fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True)

ax1.pcolormesh(xedges, yedges, H, cmap='rainbow')
ax1.plot(x, 2*np.log(x), 'k-')
ax1.set_xlim(x.min(), x.max())
ax1.set_ylim(y.min(), y.max())
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('histogram2d')
ax1.grid()

# Create hexbin plot for comparison
ax2.hexbin(x, y, gridsize=20, cmap='rainbow')
ax2.plot(x, 2*np.log(x), 'k-')
ax2.set_title('hexbin')
ax2.set_xlim(x.min(), x.max())
ax2.set_xlabel('x')
ax2.grid()

plt.show()
