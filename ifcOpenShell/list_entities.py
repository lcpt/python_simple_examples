import ifcopenshell
import sys

#inputFileName= sys.argv[1]
inputFileName= './beams.ifc'

ifc_file = ifcopenshell.open(inputFileName)
products = ifc_file.by_type('IfcProduct')
beams= list()
for product in products:
    print(product.is_a())
    if(product.is_a('IfcBeamStandardCase')):
        beams.append(product)

for b in beams:
    print('beam Description:', b.Description)
        
