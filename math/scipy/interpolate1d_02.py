# -*- coding: utf-8 -*-
'''Extrapolation of pile resistances.'''

# import matplotlib.pyplot as plt
from scipy import interpolate

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2025, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

numberOfDiameters= [3, 4, 5, 6, 7, 8, 9]
qpPileResistance= [4991e3, 5812e3, 6632e3, 7452e3, 7813e3, 7918e3, 7918e3] 
rarePileResistance= [5820e3, 6775e3, 7730e3, 8685e3, 8710e3, 8710e3, 8710e3]

fQpPileResistance= interpolate.interp1d(numberOfDiameters, qpPileResistance, fill_value='extrapolate')
fRarePileResistance= interpolate.interp1d(numberOfDiameters, rarePileResistance, fill_value='extrapolate')

print('Combinación cuasi-permanente, resistencia: ', fQpPileResistance(2.46)/1e3, ' kN')
print('Combinación característica, resistencia: ', fRarePileResistance(2.46)/1e3, ' kN')

# fig, ax = plt.subplots()
# ax.plot(numberOfDiameters, qpPileResistance)
# ax.plot(numberOfDiameters, rarePileResistance)

# ax.set(xlabel='nD', ylabel='Q (kN)',
#        title='Carga vertical admisible')
# ax.grid()
 
# # Show graph
# #fig.savefig("test.png")
# plt.show()
