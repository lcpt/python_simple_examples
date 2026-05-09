#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtk.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtk.vtkRenderingOpenGL2
from vtk.vtkCommonColor import vtkNamedColors
from vtk.vtkCommonCore import vtkPoints
from vtk.vtkCommonDataModel import vtkPolyData
from vtk.vtkFiltersCore import (
    vtkGlyph3D,
    vtkAppendPolyData,
    vtkCleanPolyData
)
from vtk.vtkFiltersSources import (
    vtkCubeSource,
    vtkConeSource
    )
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

    polydata = vtkPolyData()
    polydata.SetPoints(points)

    # Create anything you want here, we will use a cube for the demo.
    cube = vtkCubeSource()
    cube.Update()
    input1= vtkPolyData()
    input1.ShallowCopy(cube.GetOutput())

    cone = vtkConeSource()
    # cone.SetResolution(5)
    cone.SetHeight(4.0)
    cone.Update()
    input2= vtkPolyData()
    input2.ShallowCopy(cone.GetOutput())

    # Append the two meshes
    appendFilter= vtkAppendPolyData()
    appendFilter.AddInputData(input1)
    appendFilter.AddInputData(input2)
    appendFilter.Update()
  
    #  Remove any duplicate points.
    cleanFilter= vtkCleanPolyData()
    cleanFilter.SetInputConnection(appendFilter.GetOutputPort())
    cleanFilter.Update()


    glyph3D = vtkGlyph3D()
    # glyph3D.SetSourceConnection(cube.GetOutputPort())
    glyph3D.SetSourceConnection(cleanFilter.GetOutputPort())
    # glyph3D.SetInputConnection(cone.GetOutputPort())
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
