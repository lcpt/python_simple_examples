# -*- coding: utf-8 -*-

import FreeCAD
import Part

doc = App.newDocument("Techdraw section")
cubeShape = Part.makeBox(2, 2, 2)
cube= Part.show(cubeShape)
cube.Label= 'cube'

cone = doc.addObject("Part::Cone", "cone")
cone.Radius1 = 5
cone.Radius2 = 0
cone.Height = 3
cone.Angle = 270
cone.Placement = App.Placement(App.Vector(1, 1, 3), App.Rotation(0, 0, 0))

box= doc.Shape
page= doc.addObject('TechDraw::DrawPage','Page')
template= doc.addObject('TechDraw::DrawSVGTemplate','Template')
template.Template= App.ConfigGet('AppHomePath')+'Mod/Drawing/Templates/A1_Landscape_blank.svg'
page.Template= template

view = activeDoc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = box
view.Direction = (0, 0, 1)

section = doc.addObject("TechDraw::DrawViewSection", "Section")
page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0, 1, 0)
section.SectionNormal = (-1, 0, 0)

doc.recompute()
