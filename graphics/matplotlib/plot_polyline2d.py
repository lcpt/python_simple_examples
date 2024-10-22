# Example taken from https://stackoverflow.com/questions/45817646/how-to-plot-polyline-in-3d-in-python

# libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# create dataset
x = [1, 1, 0, 2]
y = [0, 1, 1, 2]
 
fig = plt.figure()
ax = plt.axes()

ax.plot(x, y)

# Show graph
plt.show()
