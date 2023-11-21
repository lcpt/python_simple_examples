#!/usr/bin/env python

import vtk

def main():
    colors = vtk.vtkNamedColors()

    # Create 5 points (vtkPolyData)
    pointSource = vtk.vtkPointSource()
    pointSource.SetNumberOfPoints(5)
    pointSource.Update()

    polydata = pointSource.GetOutput()

    print('There are', polydata.GetNumberOfPoints(), 'points in the polydata.')

    # Create 2 points in a vtkUnstructuredGrid
    points = vtk.vtkPoints()
    points.InsertNextPoint(0, 0, 0)
    points.InsertNextPoint(0, 0, 1)

    ug = vtk.vtkUnstructuredGrid()
    ug.SetPoints(points)
    print('There are', ug.GetNumberOfPoints(), 'points in the unstructured.')

    # Combine the two data sets
    appendFilter = vtk.vtkAppendFilter()
    appendFilter.AddInputData(polydata)
    appendFilter.AddInputData(ug)
    appendFilter.Update()

    combined = vtk.vtkUnstructuredGrid()

    combined = appendFilter.GetOutput()
    print('There are', combined.GetNumberOfPoints(), 'points combined.')

    # Create a mapper and actor
    mapper = vtk.vtkDataSetMapper()
    mapper.SetInputConnection(appendFilter.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetPointSize(5)

    # Map the points to spheres
    sphereActor = point_to_glyph(appendFilter.GetOutput().GetPoints(), 0.05)
    sphereActor.GetProperty().SetColor(colors.GetColor3d("Gold"))

    # Create a renderer, render window, and interactor
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    renderer.AddActor(actor)
    renderer.AddActor(sphereActor)
    renderer.SetBackground(colors.GetColor3d('RoyalBlue'))

    # Render and interact
    renderWindow.SetWindowName('AppendFilter')
    renderWindow.Render()
    renderWindowInteractor.Start()


def point_to_glyph(points, scale):
    """
    Convert points to glyphs.
    :param points: The points to glyph.
    :param scale: The scale, used to determine the size of the
                  glyph representing the point, expressed as a
                  fraction of the largest side of the bounding
                  box surrounding the points. e.g. 0.05
    :return: The actor.
    """

    bounds = points.GetBounds()
    max_len = 0.0
    for i in range(0, 3):
        max_len = max(bounds[i + 1] - bounds[i], max_len)

    sphere_source = vtk.vtkSphereSource()
    sphere_source.SetRadius(scale * max_len)

    pd = vtk.vtkPolyData()
    pd.SetPoints(points)

    mapper = vtk.vtkGlyph3DMapper()
    mapper.SetInputData(pd)
    mapper.SetSourceConnection(sphere_source.GetOutputPort())
    mapper.ScalarVisibilityOff()
    mapper.ScalingOff()

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor


if __name__ == '__main__':
    main()
