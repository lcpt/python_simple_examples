# -*- coding: utf-8 -*-
''' Read DXF file.'''

from __future__ import division
from __future__ import print_function

import sys
import ezdxf
import geom

try:
    doc = ezdxf.readfile("read_3dfaces_from_dxf.dxf")
except IOError:
    print(f"Not a DXF file or a generic I/O error.")
    sys.exit(1)
except ezdxf.DXFStructureError:
    print(f"Invalid or corrupted DXF file.")
    sys.exit(2)

# Get polygons.
dxfPolygons= list()
msp = doc.modelspace()
for e in msp:
    if(e.dxf.layer == '0'):
        if(e.dxftype() == '3DFACE'):
            newPolygon= list()
            for pt in [e.dxf.vtx0, e.dxf.vtx1, e.dxf.vtx2, e.dxf.vtx3]:
                newPolygon.append((pt[0], pt[1]))
            dxfPolygons.append(newPolygon)


print('3DFACEs areas:')
print('==============')
polygons= list()
for i, dxfPlg in enumerate(dxfPolygons):
    points= list()
    for (x, y) in dxfPlg:
        points.append(geom.Pos2d(x,y))
    plg= geom.Polygon2d(points)
    print(i, plg.getArea())
        
