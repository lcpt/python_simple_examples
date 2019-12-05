import ifcopenshell
# from importIFC
from ifcopenshell import geom
settings = ifcopenshell.geom.settings()
settings.set(settings.USE_BREP_DATA,True)
settings.set(settings.SEW_SHELLS,True)
settings.set(settings.USE_WORLD_COORDS,True)
settings.set(settings.INCLUDE_CURVES,True)     # for stuct

# open file
file_path = './'

f1 = ifcopenshell.open(file_path + 'export-struct.ifc')
# check if the file was load, IFCPERSON  should be in any ifc
f1.by_type('ifcperson')

f1.by_id(607)
ifcopenshell.geom.create_shape(settings, f1.by_id(607))

