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

# Create face to orient section.
extension= 7
origin= FreeCAD.Vector(1.25, 0, 0)
dirVector= FreeCAD.Vector(1, 1, 0).normalize()
kVector= FreeCAD.Vector(0,0,1)
p1= origin-extension*dirVector
p2= origin+extension*dirVector
p3= p1+extension*kVector
p4= p2+extension*kVector
cutFace= Draft.makeWire([p1, p2, p4, p3], closed= True)
cutFace.Label= 'cutFace'
cutFace.recompute()

jVector= cutFace.Shape.normalAt(0,0)
center= cutFace.Shape.CenterOfMass
cutPlanePlacement= FreeCAD.Placement(center,FreeCAD.Rotation(kVector,jVector))


# Create arch section.
# Activate Draft workbench (otherwise there is no active working plane). 
FreeCADGui.activateWorkbench("DraftWorkbench")

Section1 = Arch.makeSectionPlane([cube, cone], name= 'Section1')
Section1.Placement= cutPlanePlacement
Section1.recompute()
# print(Section1.Objects)

# You can use Section1 as argument of Shape2DView to create the section.
