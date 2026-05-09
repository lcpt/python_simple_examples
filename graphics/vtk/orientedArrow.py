import vtk
 
#arrowSource.SetShaftRadius(0.01)
#arrowSource.SetTipLength(.9)

 
vtk.vtkMath.RandomSeed(8775070)
x0= vtk.vtkMath.Random(-10,10)
y0= vtk.vtkMath.Random(-10,10)
z0= vtk.vtkMath.Random(-10,10)
startPoint= [x0, y0, z0]
x1= vtk.vtkMath.Random(-10,10)
y1= vtk.vtkMath.Random(-10,10)
z1= vtk.vtkMath.Random(-10,10)
endPoint= [x1, y1, z1]

def get_oriented_arrow_actor(startPoint, endPoint):
    ''' Return an actor to represent the oriented arrow.

    :param startPoint: arrow start point.
    :param endPoint: arrow end point.
    '''
    arrowSource = vtk.vtkArrowSource()

    #Compute a basis
    normalizedX= [0.0,0.0,0.0]
    vtk.vtkMath.Subtract(endPoint,startPoint,normalizedX)
    length= vtk.vtkMath.Norm(normalizedX)
    vtk.vtkMath.Normalize(normalizedX)


    #The Z axis is an arbitrary vector cross X
    x2= vtk.vtkMath.Random(-10,10)
    y2= vtk.vtkMath.Random(-10,10)
    z2= vtk.vtkMath.Random(-10,10)
    arbitrary= [x2, y2, z2]
    normalizedZ= [0.0,0.0,0.0]
    vtk.vtkMath.Cross(normalizedX, arbitrary, normalizedZ);
    vtk.vtkMath.Normalize(normalizedZ);

    #The Y axis is Z cross X
    normalizedY= [0.0,0.0,0.0]
    vtk.vtkMath.Cross(normalizedZ, normalizedX, normalizedY);

    #Create the direction cosine matrix
    matrix= vtk.vtkMatrix4x4()
    matrix.Identity()
    for i in range(0,3):
        matrix.SetElement(i, 0, normalizedX[i])
        matrix.SetElement(i, 1, normalizedY[i])
        matrix.SetElement(i, 2, normalizedZ[i])

    print(matrix)

    #Create the transform
    transform= vtk.vtkTransform()
    transform.Translate(startPoint)
    transform.Concatenate(matrix)
    transform.Scale(length,length,length)

    #Transform the polydata
    transformPD= vtk.vtkTransformPolyDataFilter()
    transformPD.SetTransform(transform);
    transformPD.SetInputConnection(arrowSource.GetOutputPort());

    # Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(transformPD.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    return actor

actor= get_oriented_arrow_actor(startPoint, endPoint)

# Visualize
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
 
renderer.AddActor(actor)
renderer.SetBackground(.1, .2, .3) # Background color dark blue
 
renderWindow.Render()
renderWindowInteractor.Start()
