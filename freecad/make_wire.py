# -*- coding: utf-8 -*-

import FreeCAD
import Draft

doc = FreeCAD.newDocument()

pI1 = FreeCAD.Vector(7368.163e3, 5455.858e3, 590.250e3)
pI2 = FreeCAD.Vector(7385.538e3, 5460.449e3, 590.250e3)
pI3 = FreeCAD.Vector(7498.333e3, 5492.205e3, 590.250e3)
leftAxisPoints= [pI1, pI2, pI3]

wireI = Draft.make_wire(leftAxisPoints, closed=False)
wireI.Label= 'eje_encep_izdo'

pD1 = FreeCAD.Vector(7391.231e3, 5436.835e3, 590.250e3)
pD2 = FreeCAD.Vector(7489.167e3, 5463.952e3, 590.250e3)
pD3 = FreeCAD.Vector(7533.019e3, 5477.505e3, 590.250e3)

wireD = Draft.make_wire([pD1, pD2, pD3], closed=False)
wireD.Label= 'eje_encep_dcho'


doc.recompute()
