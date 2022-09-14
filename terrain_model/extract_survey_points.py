# -*- coding: utf-8 -*-
''' Extract survey points from DXF file.'''

import sys
from pathlib import Path
import logging
import ezdxf

__author__= "Luis Claudio Pérez Tato (LCPT"
__copyright__= "Copyright 2020, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

if(len(sys.argv)<2):
    logging.error('Syntax: '+sys.argv[0]+ ' input_file_name')
    quit()


inputFileName= sys.argv[1]

try:
    doc = ezdxf.readfile(inputFileName)
except IOError:
    print(f"Not a DXF file or a generic I/O error.")
    sys.exit(1)
except ezdxf.DXFStructureError:
    print(f"Invalid or corrupted DXF file.")
    sys.exit(2)

layersToImport= ['C-PUNTOS', 'C-SUPE_CurvasNivel', 'C-SUPE_CurvasMaestras']
    
# get points surface.
surveyPoints= list()
msp = doc.modelspace()
for e in msp:
    if(hasattr(e.dxf,'layer')):
        if(e.dxf.layer in layersToImport):
            dxfType= e.dxftype()
            if(dxfType == 'INSERT'):
                surveyPoints.append((e.dxf.insert.x,e.dxf.insert.y,e.dxf.insert.z))
            elif(dxfType == 'LWPOLYLINE'):
                elevation= e.dxf.elevation
                with e.points("xyseb") as points:
                    for pt in points:
                        surveyPoints.append((pt[0],pt[1],elevation))
            elif(dxfType == 'LINE'):
                surveyPoints.append(e.dxf.start)
                surveyPoints.append(e.dxf.end)

#print(surveyPoints)
baseName= Path(inputFileName).stem
outputFileName= baseName+'.asc'
outputFile= open(outputFileName, 'w')
for id, pt in enumerate(surveyPoints):
    outputFile.write('p'+str(id)+' '+str(pt[0])+' '+str(pt[1])+' '+str(pt[2])+'\n')
outputFile.close()
