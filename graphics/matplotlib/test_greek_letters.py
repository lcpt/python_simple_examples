# -*- coding: utf-8 -*-
''' Greek letters in matplotlib labels.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2022"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@gmail.com"

import math
import numpy as np
from actions.roadway_traffic import EC1_load_models

xi= [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12.]
yi= [1.3, 1.25, 1.2, 1.15, 1.1, 1.05, 1.0, 1, 1, 1, 1, 1, 1]

import matplotlib.pyplot as plt
plt.title("Additional amplification factor.")
plt.xlabel("D")
plt.ylabel(r'$\Delta \varphi_{fat}$')
plt.plot(xi, yi)
plt.grid()
plt.show()
