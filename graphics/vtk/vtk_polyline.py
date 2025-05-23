#!/usr/bin/env python
# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences
import vtk.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtk.vtkRenderingOpenGL2
from vtk.vtkCommonColor import vtkNamedColors
from vtk.vtkCommonCore import vtkPoints
from vtk.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData,
    vtkPolyLine
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

    # Create five points.
    origin = [0.0, 0.0, 0.0]
    p0 = [1.0, 0.0, 0.0]
    p1 = [0.0, 1.0, 0.0]
    p2 = [0.0, 1.0, 2.0]
    p3 = [1.0, 2.0, 3.0]

    # Create a vtkPoints object and store the points in it
    points = vtkPoints()
    points.InsertNextPoint(origin)
    points.InsertNextPoint(p0)
    points.InsertNextPoint(p1)
    points.InsertNextPoint(p2)
    points.InsertNextPoint(p3)

    polyLine = vtkPolyLine()
    polyLine.GetPointIds().SetNumberOfIds(5)
    for i in range(0, 5):
        polyLine.GetPointIds().SetId(i, i)

    # Create a cell array to store the lines in and add the lines to it
    cells = vtkCellArray()
    cells.InsertNextCell(polyLine)

    # Create a polydata to store everything in
    polyData = vtkPolyData()

    # Add the points to the dataset
    polyData.SetPoints(points)

    # Add the lines to the dataset
    polyData.SetLines(cells)

    # Setup actor and mapper
    mapper = vtkPolyDataMapper()
    mapper.SetInputData(polyData)

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetLineWidth(5)
    actor.GetProperty().SetColor(colors.GetColor3d('Tomato'))

    # Setup render window, renderer, and interactor
    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.SetWindowName('PolyLine')
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('DarkOliveGreen'))

    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()
