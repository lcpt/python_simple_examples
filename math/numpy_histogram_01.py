import numpy as np    
hist, bin_edges = np.histogram([1, 1, 2, 2, 2, 2, 3], bins = range(5))
print(hist)

import matplotlib.pyplot as plt
plt.bar(bin_edges[:-1], hist, width = 1)
plt.xlim(min(bin_edges), max(bin_edges))
plt.show()   
