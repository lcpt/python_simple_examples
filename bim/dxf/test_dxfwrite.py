from dxfwrite import DXFEngine as dxf

drawing = dxf.drawing('test.dxf')
drawing.add_layer('LINES')
drawing.add(dxf.line((0, 0), (1, 0), color=7, layer='LINES'))
drawing.save()

