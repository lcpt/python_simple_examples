# Example of how to use range clamping with vtkGlyph3D filter.
#
# Note that the internal algorithm does this to figure out the eventual scale
# of your data (say, if you're scaling by a scalar or vector magnitude):
#
# 	scale = (scalar value of that particular data index);
# 	denominator = Range[1] - Range[0];
# 	scale = (scale < Range[0] ? Range[0] : (scale > Range[1] ? Range[1] : scale));
# 	scale = (scale - Range[0]) / denominator;
# 	scale *= scaleFactor;
#
# So, step 4 is the unintuitive one. Say your data varies from [0, 1] and you set the
# Range to [0.5, 1]. Everything below 0.5 will be mapped to 0. If you want to set a
# minimum size to your glyphs, then you can set the Range as something like [-0.5, 1]
 
 
import vtk
import math
 
# Generate an image data set with multiple attribute arrays to probe and view
# We will glyph these points with cones and scale/orient/color them with the 
# various attributes
 
# Points.
points= vtk.vtkPoints()
points.InsertNextPoint(0,0,0)
points.InsertNextPoint(5,5,5)
points.InsertNextPoint(10,10,10)
polydata= vtk.vtkPolyData()
polydata.SetPoints(points)

#Vectors at the points.
vectors= vtk.vtkDoubleArray()
vectors.SetName('Vectors')
vectors.SetNumberOfComponents(3)
vectors.InsertNextTuple3(1,1,1)
vectors.InsertNextTuple3(2,2,2)
vectors.InsertNextTuple3(3,3,3)
polydata.GetPointData().AddArray(vectors)

lengths= vtk.vtkDoubleArray()
lengths.SetName('Length')
lengths.SetNumberOfValues(3);
lengths.SetValue(0, math.sqrt(1*1+1*1+1*1))
lengths.SetValue(1, math.sqrt(2*2+2*2+2*2))
lengths.SetValue(2, math.sqrt(3*3+3*3+3*3))
polydata.GetPointData().AddArray(lengths)

colors= vtk.vtkDoubleArray()
colors.SetName('Z')
colors.SetNumberOfValues(3);
colors.SetValue(0, 1);
colors.SetValue(1, 2);
colors.SetValue(2, 3);
polydata.GetPointData().AddArray(colors)


# Generate the arrow for the glyphs
arrow = vtk.vtkArrowSource()#vtk.vtkConeSource()
#arrow.SetRadius(0.1)
#arrow.SetHeight(0.5)
 
# Set up the glyph filter
glyph = vtk.vtkGlyph3D()
glyph.SetInputData(polydata)
glyph.SetSourceConnection(arrow.GetOutputPort())
glyph.ScalingOn()
glyph.SetScaleModeToScaleByScalar()
glyph.SetVectorModeToUseVector()
glyph.OrientOn()
 
# Tell the filter to "clamp" the scalar range
#glyph.ClampingOn()  
 
# Set the overall (multiplicative) scaling factor
glyph.SetScaleFactor(1)
 
# Set the Range to "clamp" the data to 
#   -- see equations above for nonintuitive definition of "clamping"
# The fact that I'm setting the minimum value of the range below
#   the minimum of my data (real min=0.0) with the equations above
#   forces a minimum non-zero glyph size.
 
#glyph.SetRange(-10, 10)    # Change these values to see effect on cone sizes
 
# Tell glyph which attribute arrays to use for what
glyph.SetInputArrayToProcess(0,0,0,0,'Length')	# scalars
glyph.SetInputArrayToProcess(1,0,0,0,'Vectors') # vectors
# glyph.SetInputArrayToProcess(2,0,0,0,'nothing')	# normals
#glyph.SetInputArrayToProcess(3,0,0,0,'Length')		# colors
 
# Calling update because I'm going to use the scalar range to set the color map range
glyph.Update()
 
coloring_by = 'Length'
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(glyph.GetOutputPort())
mapper.SetScalarModeToUsePointFieldData()
mapper.SetColorModeToMapScalars()
mapper.ScalarVisibilityOn()
mapper.SetScalarRange(glyph.GetOutputDataObject(0).GetPointData().GetArray(coloring_by).GetRange())
mapper.SelectColorArray(coloring_by)
actor = vtk.vtkActor()
actor.SetMapper(mapper)
 
ren = vtk.vtkRenderer()
ren.AddActor(actor)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
#istyle = vtk.vtkInteractorStyleTrackballCamera()
#iren.SetInteractorStyle(istyle)
iren.SetRenderWindow(renWin)
ren.ResetCamera()
renWin.Render()
 
iren.Start()
