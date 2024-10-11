import numpy as np
from scipy.spatial import KDTree

pts = np.array([[1, 1, 0], [2, 1, 1], [3, 1, 2], [4, 1, 3], [1, 2, 4], [2, 2, 5], [3, 2, 6], [4, 2, 7], [1, 3, 8], [2, 3, 9], [3, 3, 10], [4, 3, 11], [1, 4, 12], [2, 4, 13], [3, 4, 14], [4, 4, 15]])

kdtree= KDTree(pts)
dd, idx = kdtree.query([[4.1,1,3.01]], k= 1)
print(dd, idx, pts[idx[0]])
