import numpy as np
x = [.1, .2, .5, .6, .7, .8, .9] # dx varies
y = [1, 2, 3, 4, 4, 5, 6]
y_dot= list(np.gradient(y, x)) # dy/dx 2nd order accurate

print(y_dot)
import matplotlib.pyplot as plt

# Create figure
fig, ax = plt.subplots()
ax.plot(x, y, label= '$y$')
ax.plot(x, y_dot, label= "$y'$")
ax.legend(loc="upper left")
ax.set(xlabel='x', ylabel='y', title='Gradient demo.')
ax.grid()

# Show graph
#fig.savefig("test.png")
plt.show()
