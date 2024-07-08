import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlim3d(0, 0.8)
ax.set_ylim3d(0, 0.8)
ax.set_zlim3d(0, 0.8)
ax.quiver(0, 0, 0, 1, 1, 1, length = 0.5, normalize = False)
plt.show()
