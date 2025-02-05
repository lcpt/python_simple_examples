'''
Template file with the VTK modules that are used the most. The only purpose
of this file is to make easier the inclusion of VTK modules and avoid importing
the whole vtk Python module.
'''

from vtk.vtkCommonCore import (
    vtkDoubleArray,
    vtkIntArray,
    vtkStringArray,
    vtkLookupTable,
    vtkMinimalStandardRandomSequence,
    vtkIdList,
    vtkPoints
    )
from vtk.vtkCommonDataModel import (
    vtkPolyData,
    vtkCellArray,
    vtkUnstructuredGrid
  )
from vtk.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
    vtkWindowToImageFilter,
    vtkGlyph3DMapper,    
    vtkActor2D,
    vtkDataSetMapper,
    vtkTextMapper,
    vtkTextProperty,
    vtkSelectVisiblePoints
)
from vtk.vtkFiltersSources import (
    vtkArrowSource,
    vtkSphereSource,
    vtkConeSource,
    vtkCubeSource,
    vtkCylinderSource,
    # vtkCellTypeSource,
    vtkPlaneSource
    )
from vtk.vtkIOImage import vtkPNGWriter
from vtk.vtkIOImage import vtkJPEGWriter
from vtk.vtkRenderingAnnotation import vtkCornerAnnotation
from vtk.vtkCommonColor import (
    vtkColorSeries,
    vtkNamedColors
)
from vtk.vtkCommonDataModel import (
    VTK_CUBIC_LINE,
    VTK_HEXAHEDRON,
    VTK_LINE,
    VTK_PYRAMID,
    VTK_QUAD,
    VTK_QUADRATIC_EDGE,
    VTK_QUADRATIC_HEXAHEDRON,
    VTK_QUADRATIC_PYRAMID,
    VTK_QUADRATIC_QUAD,
    VTK_QUADRATIC_TETRA,
    VTK_QUADRATIC_TRIANGLE,
    VTK_QUADRATIC_WEDGE,
    VTK_TETRA,
    VTK_TRIANGLE,
    VTK_VERTEX,
    VTK_WEDGE,
    vtkCellTypes
)
from vtk.vtkFiltersGeneral import (
    vtkShrinkFilter,
    vtkCellCenters,
    vtkTessellatorFilter
)
from vtk.vtkFiltersCore import (
    vtkGlyph3D,
    vtkFeatureEdges,
    # vtkGenerateIds,
    vtkIdFilter
)
from vtk.vtkRenderingLabel import (
    vtkLabelPlacementMapper,
    vtkLabeledDataMapper,
    vtkPointSetToLabelHierarchy,
)
