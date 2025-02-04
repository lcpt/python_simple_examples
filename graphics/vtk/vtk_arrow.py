#!/usr/bin/env python

# noinspection PyUnresolvedReferences
import vtk.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtk.vtkRenderingOpenGL2
from vtk.vtkCommonColor import vtkNamedColors
from vtk.vtkFiltersSources import vtkArrowSource
from vtk.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)


def main():
    colors = vtkNamedColors()

    arrowSource = vtkArrowSource()
    # arrowSource.SetShaftRadius(0.01)
    # arrowSource.SetTipLength(.9)

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(arrowSource.GetOutputPort())
    actor = vtkActor()
    actor.SetMapper(mapper)

    # Visualize
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Arrow')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('MidnightBlue'))

    renderWindow.SetWindowName('Arrow')
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
