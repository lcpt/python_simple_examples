#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtk.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtk.vtkRenderingOpenGL2
from vtk.vtkCommonColor import vtkNamedColors
from vtk.vtkCommonCore import vtkPoints
from vtk.vtkCommonDataModel import vtkPolyData
from vtk.vtkFiltersCore import vtkGlyph3D
from vtk.vtkFiltersSources import vtkCubeSource
from vtk.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)


def main():
    colors = vtkNamedColors()

    points = vtkPoints()
    points.InsertNextPoint(0, 0, 0)
    points.InsertNextPoint(1, 1, 1)
    points.InsertNextPoint(2, 2, 2)

    polydata = vtkPolyData()
    polydata.SetPoints(points)

    # Create anything you want here, we will use a cube for the demo.
    cubeSource = vtkCubeSource()

    glyph3D = vtkGlyph3D()
    glyph3D.SetSourceConnection(cubeSource.GetOutputPort())
    glyph3D.SetInputData(polydata)
    glyph3D.Update()

    # Visualize
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(glyph3D.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Salmon'))

    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('SlateGray'))  # Background Slate Gray

    renderWindow.SetWindowName('Glyph2D');
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
