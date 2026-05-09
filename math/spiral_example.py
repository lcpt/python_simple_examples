# -*- coding: utf-8 -*-
''' Plot a spiral.'''

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0., 8*np.pi, 1000)
a, b = 0, 2.
plt.polar(theta, a+b*theta)
plt.show()
