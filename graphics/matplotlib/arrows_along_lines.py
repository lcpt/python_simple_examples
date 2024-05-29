# -*- coding: utf-8 -*-
''' Plot arrows along lines.

Code inspired by: https://stackoverflow.com/questions/58342419/show-direction-arrows-in-a-scatterplot
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame.from_dict({'x' : [0,3,8,7,5,3,2,1],
                             'y' : [0,1,3,5,9,8,7,5]})
x = df['x'].values
y = df['y'].values

u = np.diff(x)
v = np.diff(y)
pos_x = x[:-1] + u/2
pos_y = y[:-1] + v/2
norm = np.sqrt(u**2+v**2) 

fig, ax = plt.subplots()
ax.plot(x,y, marker="o")
ax.quiver(pos_x, pos_y, u/norm, v/norm, angles="xy", zorder=5, pivot="mid")
plt.show()
