import ifcopenshell
import sys

#inputFileName= sys.argv[1]
inputFileName= './IfcOpenHouse.ifc'
outputFileName= './IfcOpenHouse_roof.ifc'

ifc_file = ifcopenshell.open(inputFileName)
outputModel= ifcopenshell.file(schema=ifc_file.schema)
ifcProject= ifc_file.by_type("IfcProject")[0]
outputModel.add(ifcProject)

selectedProducts= list()
for product in ifc_file.by_type("IfcBuildingElement"):
    # print(product.is_a())
    if(product.is_a('IfcSlab')):
        print(product.Name)
        selectedProducts.append(product)

for product in selectedProducts:
    outputModel.add(product)
    
outputModel.write(outputFileName)
