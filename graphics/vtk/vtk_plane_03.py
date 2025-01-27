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
    planeSource.SetNormal(1.0, 0.0, 0.0)
    # planeSource.SetCenter(0.0, 0.5, -0.5)
    planeSource.Update()
    
    print('normal= ', planeSource.GetNormal())
    print('origin= ', planeSource.GetOrigin())
    print('center= ', planeSource.GetCenter())

    plane = planeSource.GetOutput()

    # Create a mapper and actor
    mapper = vtkPolyDataMapper()
    mapper.SetInputData(plane)

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Banana'))

    axes = vtk.vtkAxesActor()
    
    # Create a renderer, render window and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('Plane')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actors to the scene
    renderer.AddActor(actor)
    renderer.AddActor(axes)
    renderer.SetBackground(colors.GetColor3d('BkgColor'))

    # Render and interact
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
