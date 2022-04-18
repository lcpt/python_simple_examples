import vtk
 
lookupTable= vtk.vtkLookupTable()
 
# lookupTable.SetTableRange(0.0, 10.0)
# # If you don't want to use the whole color range, you can use
# # SetValueRange, SetHueRange, and SetSaturationRange
# lookupTable.Build()

lookupTable.SetNumberOfTableValues(2)
lookupTable.SetTableValue(0,[0.0,0.0,1.0,0.0])
lookupTable.SetTableValue(1,[0.0,0.0,1.0,0.0])

color= [0,0,0]
lookupTable.GetColor(0.0,color)
print color
 
lookupTable.GetColor(5.0,color)
print color

lookupTable.GetColor(10.0,color)
print color
 
