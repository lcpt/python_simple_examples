# -*- coding: utf-8 -*-
''' Read DXF file.'''

from __future__ import division
from __future__ import print_function

import sys
import ezdxf

inputFileName= 'test_color2layer_input.dxf'
outputFileName= 'test_color2layer_output.dxf'

# Test color conversion.
colorConversion= dict()
for i in range(0,256):
    colorConversion[i]= {'newLayer': 'color_'+str(i), 'newColor':255-i, 'newLType':'CONTINUOUS'}

try:
    doc = ezdxf.readfile(inputFileName)
except IOError:
    print(f"Not a DXF file or a generic I/O error.")
    sys.exit(1)
except ezdxf.DXFStructureError:
    print(f"Invalid or corrupted DXF file.")
    sys.exit(2)

# create layers.
## Compute new layer names.
layerNames= dict()
msp = doc.modelspace()
for e in msp:
    objectColor= e.dxf.color
    newLayer= colorConversion[objectColor]['newLayer']
    newColor= colorConversion[objectColor]['newColor']
    newLType= colorConversion[objectColor]['newLType']
    if(newLayer not in layerNames):
        layerNames[newLayer]= {'newColor':newColor, 'newLType':'CONTINUOUS'}

## Create layers.
for key in layerNames:
    data= layerNames[key]
    newLayer= doc.layers.new(name= key)
    newLayer.color= data['newColor']
    newLayer.linetype= data['newLType']

## Set the objects layer.
for e in msp:
    objectColor= e.dxf.color
    e.dxf.layer= colorConversion[objectColor]['newLayer']

# Save the modified DXF document.
doc.saveas(outputFileName)
