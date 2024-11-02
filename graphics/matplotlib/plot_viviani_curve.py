import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# The cylinder radius; the intersecting sphere has radius 2a.
a = 1

# Number of points of the parametric function to calculate.
n = 100
t = np.linspace(0, 4*np.pi, n)
# Cartesian coordinates of the Viviani curve.
x = a * (1 + np.cos(t))
y = a * np.sin(t)
z = 2 * a * np.sin(t/2)

fig = plt.figure(figsize=plt.figaspect(1.))
ax = fig.add_subplot(111, projection='3d')

# Outline the intersecting sphere and cylinder in light grey circles.
ng = n//2 + 1
# We only need to go from 0 to 2π for circles!
theta = t[:ng]
for phi in np.linspace(-np.pi,np.pi,32):
    # Circles on the sphere in two perpendicular planes.
    ax.plot(2*a*np.sin(theta)*np.cos(phi), 2*a*np.cos(theta)*np.cos(phi),
        2*a*np.sin(phi), 'gray', alpha=0.2, lw=1)
    ax.plot(2*a*np.cos(theta)*np.cos(phi), [2*a*np.sin(phi)]*ng,
        2*a*np.sin(theta)*np.cos(phi), 'gray', alpha=0.2,lw=1)
    # The circles of the cylinder.
    ax.plot(a*np.sin(theta)+a, a*np.cos(theta), 2*a*phi/np.pi,
            'm', alpha=0.2, lw=1)

ax.plot(x, y, z, 'r', lw=4)

# Tidy up by switching off the axes and setting the view orientation.
ax.set_axis_off()
ax.view_init(0, 50)
# plt.savefig('viviani.png')
plt.show()
