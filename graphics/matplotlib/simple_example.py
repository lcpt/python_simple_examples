# -*- coding: utf-8 -*-
'''Simple example taken from https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html'''

# libraries
import matplotlib.pyplot as plt
import numpy as np
 
# create dataset
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
 
# Create figure
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()
 
# Show graph
#fig.savefig("test.png")
plt.show()
