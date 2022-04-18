import ifcopenshell
def print_quantities(property_definition):
  if 'IfcElementQuantity' == property_definition.is_a():
    for quantity in property_definition.Quantities:
      if 'IfcQuantityArea' == quantity.is_a():
        print('Area value: ' + str(quantity.AreaValue))
      if 'IfcQuantityVolume' == quantity.is_a():
        print('Volume value: ' + str(quantity.VolumeValue))
      if 'IfcQuantityLength' == quantity.is_a():
        print('Length value: ' + str(quantity.LengthValue))

ifc_file = ifcopenshell.open('export-struct.ifc')
products = ifc_file.by_type('IfcPerson')
for product in products:
  if product.IsDefinedBy:
    definitions = product.IsDefinedBy
    for definition in definitions:
      #In IFC2X3 this could be property or type
      #in IFC4 type is in inverse attribute IsTypedBy
      if 'IfcRelDefinesByProperties' == definition.is_a():
        property_definition = definition.RelatingPropertyDefinition
        print_quantities(property_definition)
      if 'IfcRelDefinesByType' == definition.is_a():
        type = definition.RelatingType
        if type.HasPropertySets:
          for property_definition in type.HasPropertySets:
            print_quantities(property_definition)
