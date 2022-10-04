import ezdxf

doc = ezdxf.new("R2000")
msp = doc.modelspace()

textAttribs= {'style': 'LiberationSerif', 'height': 0.35}
text1= msp.add_text("Text Style Example: Liberation Serif",
             dxfattribs= textAttribs
             )
text1.set_pos((2, 6), align='LEFT')

text2= msp.add_text("Right aligned text",
             dxfattribs= textAttribs
             )
text2.set_pos((2, 4), align='RIGHT')

doc.saveas("text_test.dxf")
