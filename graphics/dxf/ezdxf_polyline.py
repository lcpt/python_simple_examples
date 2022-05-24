import ezdxf

doc = ezdxf.new("R2000")
msp = doc.modelspace()

points = [(0, 0), (3, 0), (6, 3), (6, 6)]
msp.add_lwpolyline(points)

doc.saveas("lwpolyline1.dxf")
