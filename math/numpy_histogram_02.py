import numpy as np

arr = np.random.randint(1, 51, 500)
y, x = np.histogram(arr, bins=np.arange(51))

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(x[:-1], y)
plt.show()
