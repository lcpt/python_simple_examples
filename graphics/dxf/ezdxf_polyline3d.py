import ezdxf

doc = ezdxf.new("R2000")
msp = doc.modelspace()

points = [(0, 0, 0), (3, 0, 0), (6, 3, 0), (6, 6, 0)]
msp.add_polyline3d(points)

doc.saveas("polyline_3d.dxf")
