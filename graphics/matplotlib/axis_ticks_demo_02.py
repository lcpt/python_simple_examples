import numpy as np
import matplotlib.pyplot as plt

#define data
x = [0, 2, 7, 10, 12, 15, 18, 20]
y = [0, 5, 9, 13, 19, 22, 29, 36]

#create line plot
plt.plot(x,y)

#specify axis tick step sizes
plt.xticks(np.arange(min(x), max(x)+1, 2))
plt.yticks(np.arange(min(y), max(y)+1, 4))

#display line plot
plt.show()
