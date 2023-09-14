# -*- coding: utf-8 -*-
''' Script based on the one shown on the page: 
https://wiki.freecad.org/Arch_SectionPlane 
'''

import FreeCAD
import Part
import Arch
import Draft
import FreeCADGui

doc = App.newDocument("Arch section plane")

# Create cube.
cubeShape = Part.makeBox(2, 2, 2)
cube= Part.show(cubeShape)
cube.Label= 'cube'

# Create cone.
cone = doc.addObject("Part::Cone", "cone")
cone.Radius1 = 2.5
cone.Radius2 = 0
cone.Height = 3
cone.Angle = 270
cone.Placement = App.Placement(App.Vector(1, 1, 3), App.Rotation(0, 0, 0))

# Create line to orient section.
p1= FreeCAD.Vector(2, 0, 0)
p2= FreeCAD.Vector(0, 2, 0)
cutLine = Draft.makeWire([p1, p2], closed= False)
cutLine.Label= 'cutLine'
cutLine.recompute()
kVector= FreeCAD.Vector(0,0,1)
iVector= cutLine.Shape.Edges[0].tangentAt(0)
jVector= kVector.cross(iVector)
center= cutLine.Shape.CenterOfMass

cutPlanePlacement= FreeCAD.Placement(center,FreeCAD.Rotation(kVector,jVector))

# Create section.
# Activate Draft workbench (otherwise there is no active working plane). 
FreeCADGui.activateWorkbench("DraftWorkbench")

Section1 = Arch.makeSectionPlane([cube, cone], name= 'Section1')
Section1.Placement= cutPlanePlacement
Section1.Clip= False # Cut the whole model.
# print(Section1.Objects)

# You can use Section1 as argument of Shape2DView to create the section.
