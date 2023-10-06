# Example taken from https://stackoverflow.com/questions/45817646/how-to-plot-polyline-in-3d-in-python

# libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# create dataset
x = [1, 2, 3]
y = [2, 3, 4]
z = [5, 6, 7]
 
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x, y, z)

# Show graph
plt.show()
