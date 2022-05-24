import ezdxf

# Create a new DXF document.
doc = ezdxf.new(dxfversion="R2010")

# Create new table entries (layers, linetypes, text styles, ...).
#doc.layers.add("TEXTLAYER", color=2)
doc.layers.new(name="MyLines")
doc.layers.color=7
doc.layers.linetype="DASHED"

# DXF entities (LINE, TEXT, ...) reside in a layout (modelspace, 
# paperspace layout or block definition).  
msp = doc.modelspace()

# Add entities to a layout by factory methods: layout.add_...() 
msp.add_line((0, 0), (10, 0), dxfattribs={"color": 7})
msp.add_text(
    "Test", 
    dxfattribs={
        "layer": "TEXTLAYER"
    }).set_pos((0, 0.2), align="CENTER")

# Save the DXF document.
doc.saveas("test.dxf")
