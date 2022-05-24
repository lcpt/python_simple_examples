import ezdxf

# Data
beamContourPoints= [(-0.11249999999999999, 0.0), (20.1125, 0.0), (20.1125, 0.75), (-0.11249999999999999, 0.75), (-0.11249999999999999, 0.0)]

cablePoints= [(-0.11249999999999999, 0.4765994768202242), (1.0000000000000007, 0.3982961595273265), (2.000000000000001, 0.3356907927129493), (3.000000000000001, 0.2804507631708518), (4.000000000000001, 0.232576070901034), (5.000000000000001, 0.19206671590349578), (6.000000000000001, 0.15892269817823734), (7.000000000000001, 0.13314401772525847), (8.0, 0.11473067454455932), (9.0, 0.10368266863613979), (10.0, 0.09999999999999998), (11.0, 0.1036826686361399), (12.0, 0.11473067454455932), (13.0, 0.13314401772525852), (14.0, 0.15892269817823734), (15.0, 0.19206671590349578), (16.0, 0.23257607090103405), (17.0, 0.2804507631708518), (18.0, 0.3356907927129492), (19.0, 0.39829615952732655), (20.1125, 0.4765994768202241)]

# Convenience variables
textOffset= .05

# Create a new DXF document.
doc = ezdxf.new(dxfversion="R2010")

msp = doc.modelspace()

## Draw cable points.
msp.add_lwpolyline(cablePoints, dxfattribs={"layer": 'cable_axis'})
## Draw contour.
msp.add_lwpolyline(beamContourPoints, dxfattribs={"layer": 'beam'})

## Draw texts.
for p in cablePoints:
    (x,y)= p
    xText= '{:+.3f}'.format(x)
    yText= '{:+.3f}'.format(y)
    attribs= dxfattribs={"layer": "TEXTLAYER", 'height': 0.1, 'rotation': 90}
    msp.add_text(
        xText, 
        dxfattribs= attribs).set_pos((x-textOffset, -2.0), align="CENTER")
    msp.add_text(
        yText, 
        dxfattribs= attribs).set_pos((x-textOffset, -1.0), align="CENTER")
    msp.add_line((x, -2), (x, -.1), dxfattribs={"color": 2})
    
doc.saveas("ezdxf_profiles_example.dxf")
