# -*- coding: utf-8 -*-

import FreeCAD
import Part

doc = App.newDocument("Techdraw section")
cubeShape = Part.makeBox(2, 2, 2)
cube= Part.show(cubeShape)
cube.Label= 'cube'

cone = doc.addObject("Part::Cone", "cone")
cone.Radius1 = 2.5
cone.Radius2 = 0
cone.Height = 3
cone.Angle = 270
cone.Placement = App.Placement(App.Vector(1, 1, 3), App.Rotation(0, 0, 0))

page= doc.addObject('TechDraw::DrawPage','Page')
template= doc.addObject('TechDraw::DrawSVGTemplate','Template')
template.Template= App.ConfigGet('AppHomePath')+'Mod/TechDraw/Templates/A3_Landscape_blank.svg'
page.Template= template

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = [cube, cone]
view.Direction = (0, 0, 1)
view.ScaleType= u'Custom'
view.Scale= 25
# view.Rotation='90.00 deg'
# view.HardHidden= True
view.Caption='Top view'
view.recompute()


doc.recompute()
