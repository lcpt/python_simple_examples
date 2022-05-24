import ezdxf

doc = ezdxf.new(setup=True)  # setup required line types
msp = doc.modelspace()
newLayer= doc.layers.new(name="MyLines")
newLayer.color=6
newLayer.linetype="DASHED"
