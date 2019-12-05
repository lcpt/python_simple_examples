import ifcopenshell
import sys

ifc_file = ifcopenshell.open(sys.argv[1])
products = ifc_file.by_type('IfcProduct')
for product in products:
    print(product.is_a())
