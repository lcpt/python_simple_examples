# -*- coding: utf-8 -*-
''' Display a 2D point cloud.

Code inspired by: https://portwooddigital.com/2024/04/21/material-testing-with-white-noise/
'''

__author__= "Luis C. Pérez Tato (LCPT) and Ana Ortega (AO_O)"
__copyright__= "Copyright 2022, LCPT and AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es ana.ortega@ciccp.es"

import random
from scipy.stats import norm

# Create a sequence of random points.
randomSeed= random.randint(1e5,1e6-1)
random.seed(randomSeed)
Npulse= 1000 # Number of pulses
pulses= list(range(Npulse))
noise= [norm.ppf(random.random()) for i in pulses]

import matplotlib.pyplot as plt
plt.scatter(pulses, noise, marker= 'x')
plt.title('Random 2D points')
plt.xlabel('Pulse number')
plt.ylabel('Magnitude')
plt.show()
