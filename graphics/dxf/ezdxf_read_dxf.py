# -*- coding: utf-8 -*-
''' Read DXF file.'''

from __future__ import division
from __future__ import print_function

import sys
import ezdxf

try:
    doc = ezdxf.readfile("pile_wall.dxf")
except IOError:
    print(f"Not a DXF file or a generic I/O error.")
    sys.exit(1)
except ezdxf.DXFStructureError:
    print(f"Invalid or corrupted DXF file.")
    sys.exit(2)

# get backfill surface.
backfillSurfacePoints= list()
msp = doc.modelspace()
for e in msp:
    if(e.dxf.layer == 'backfill'):
        if(e.dxftype() == 'LWPOLYLINE'):
            with e.points("xyseb") as points:
                for pt in points:
                    backfillSurfacePoints.append((pt[0], pt[1]))
    if(e.dxf.layer == 'wall_back'):
        if(e.dxftype() == 'LINE'):
            wallBackTop= e.dxf.start
            wallBackBottom= e.dxf.end
            if(wallBackTop[1]<wallBackBottom[1]):
                wallBackTop, wallBackBottom= wallBackBottom, wallBackTop

backfillSurfacePoints.reverse()
print(backfillSurfacePoints)
print(wallBackTop, wallBackBottom)
