# -*- coding: utf-8 -*-
''' Read point coordinates from CSV file.'''

__author__= "Luis C. Pérez Tato (LCPT))"
__copyright__= "Copyright 2026, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@gmail.com"

import csv
import math

point_coo= list()
with open('point_coordinates.csv', 'r') as f:
    rows= list(csv.reader(f))
    for row in rows[2:]:
        pos= (float(row[0]), float(row[1]), float(row[2]))
        point_coo.append(pos)


length2D= 0.0
length3D= 0.0
p0= point_coo[0]
for p1 in point_coo[1:]:
    dist3D= math.sqrt((p1[0]-p0[0])**2+(p1[1]-p0[1])**2+(p1[2]-p0[2])**2)
    length3D+= dist3D
    dist2D= math.sqrt((p1[0]-p0[0])**2+(p1[1]-p0[1])**2)
    length2D+= dist2D
    p0= p1

print(len(point_coo), 'points read')
print('3d lenght: ', length3D)
print('2d lenght: ', length2D)

