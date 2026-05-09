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
    vtkArrowSource,
    vtkConeSource
    )
from vtk.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def get_double_headed_arrow():
    ''' Create a double headed arrow that can be set as source connection
        for a glyph.
    '''
    arrow= vtkArrowSource()
    arrow.Update()
    arrow_input= vtkPolyData()
    arrow_input.ShallowCopy(arrow.GetOutput())

    second_head= vtkConeSource()
    tip_length= arrow.GetTipLength()
    second_head.SetHeight(tip_length)
    second_head.SetRadius(arrow.GetTipRadius())
    second_head.SetResolution(arrow.GetTipResolution())
    second_head.SetCenter([1.0-1.1*tip_length,0,0])
    second_head.Update()
    second_head_input= vtkPolyData()
    second_head_input.ShallowCopy(second_head.GetOutput())

    # Append the two meshes
    appendFilter= vtkAppendPolyData()
    appendFilter.AddInputData(arrow_input)
    appendFilter.AddInputData(second_head_input)
    appendFilter.Update()
  
    #  Remove any duplicate points.
    retval= vtkCleanPolyData()
    retval.SetInputConnection(appendFilter.GetOutputPort())
    retval.Update()
    return retval
    

def main():
    colors = vtkNamedColors()

    points = vtkPoints()
    points.InsertNextPoint(0, 0, 0)

    polydata = vtkPolyData()
    polydata.SetPoints(points)


    double_headed_arrow= get_double_headed_arrow()
    glyph3D = vtkGlyph3D()
    glyph3D.SetSourceConnection(double_headed_arrow.GetOutputPort())
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
