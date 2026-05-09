#!/usr/bin/env python
# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences
import vtk.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtk.vtkRenderingOpenGL2
from vtk.vtkCommonColor import vtkNamedColors
from vtk.vtkFiltersSources import vtkPlaneSource
from vtk.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)


def main():
    colors = vtkNamedColors()

    # Set the background color.
    colors.SetColor('BkgColor', [26, 51, 77, 255])

    # Create a plane
    planeSource = vtkPlaneSource()
    planeSource.SetCenter(0.5, 0.5, 0.0)
    planeSource.SetPoint1(0.0, 1.0, 0.0)
    planeSource.SetPoint2(1.0, 0.0, 0.0)
    planeSource.Update()

    print('origin= ', planeSource.GetOrigin())

    plane = planeSource.GetOutput()

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputData(plane)

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Banana'))

    # Create a renderer, render window and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Plane')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('BkgColor'))

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
