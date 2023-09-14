# -*- coding: utf-8 -*-
''' Script based on the code shown on the page: 

https://wiki.freecad.org/Draft_SelectPlane
'''
import FreeCAD
import FreeCADGui

FreeCADGui.activateWorkbench("DraftWorkbench")
doc = FreeCAD.newDocument("Working plane setup")

workplane = FreeCAD.DraftWorkingPlane

v1 = FreeCAD.Vector(0, 0, 0)
v2 = FreeCAD.Vector(1, 1, 1).normalize()

workplane.alignToPointAndAxis(v1, v2, 17)
FreeCADGui.Snapper.toggleGrid()
FreeCADGui.Snapper.toggleGrid()
