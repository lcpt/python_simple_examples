def get_all_keys(d):
    for key, value in d.items():
        if isinstance(value, dict):
            yield from get_all_keys(value)
        else:
            yield key, value, type(value)


d = {'dict1': {'foo': 1, 'bar': 2}, 'dict2': {'dict3': {'baz': 3, 'quux': 4}}}
for x in get_all_keys(d):
    print(x)


d2= {'mainDATFile': '', 'groupDATFiles': [], 'dxfLayers': [], 'outputFileName': '/tmp/test_ifc_surface_01_blocks', 'problemName': 'FEcase', 'nodeHandlerName': 'nodes', 'cellHandlerName': 'elements', 'setHandlerName': 'groups', 'pointHandlerName': 'points', 'lineHandlerName': 'lines', 'surfaceHandlerName': 'surfaces', 'cellConversion': {}, 'meshDesc': None, 'blockData': {'name': 'test', 'materials': {}, 'points': {0: {'ident': 0, 'coords': [0.0, 0.0, 0.0], 'blockProperties': {'labels': [], 'attributes': {}}}, 1: {'ident': 1, 'coords': [1.0, 0.0, 0.0], 'blockProperties': {'labels': [], 'attributes': {}}}, 2: {'ident': 2, 'coords': [1.0, 1.0, 0.0], 'blockProperties': {'labels': [], 'attributes': {}}}, 3: {'ident': 3, 'coords': [0.0, 1.0, 0.0], 'blockProperties': {'labels': [], 'attributes': {}}}}, 'blocks': {0: {'ident': 0, 'cellType': 'face', 'nodeIds': [0, 1, 2, 3], 'thickness': 0.2, 'blockProperties': {'labels': ['IFCFace'], 'attributes': {'IfcType': 'Structural Surface Member', 'PredefinedType': 'SHELL', 'IfcProperties': {}, 'Thickness': 0.2, 'Material': 'C25', 'IfcDescription': '', 'name': 'Component', 'matId': 'C25'}}}}, 'pointSupports': {}, 'verbosity': 1}}

for x in get_all_keys(d2):
    print(x)
