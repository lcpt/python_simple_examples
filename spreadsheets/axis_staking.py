# -*- coding: utf-8 -*-
''' Imports the railway axis over the bridge.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2023, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

import pyexcel as pe

sheet = pe.get_sheet(file_name="axis_staking.ods")
columnLabels= list()
for c in sheet.row[0]:
    columnLabels.append(c.strip())

pkIndex= columnLabels.index('PK Estac.')
azimutIndex= columnLabels.index('Azimut')
xIndex= columnLabels.index('X')
yIndex= columnLabels.index('Y')
zIndex= columnLabels.index('Z')

points= list()
for row in sheet.row[1:]:
    pk= row[pkIndex]
    pkString= str(pk)
    if(len(pkString)<1):
        break
    else:
        pk= float(pk)
        azimut= float(row[azimutIndex])
        x= float(row[xIndex])
        y= float(row[yIndex])
        z= float(row[zIndex])
        points.append([pk, azimut, [x,y,z]])

for row in points:
    print('pk: ', row[0])
    print('azimut: ', row[1])
    print('position: ', row[2])
