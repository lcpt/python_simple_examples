# -*- coding: utf-8 -*-
''' Writes the the bearing resistance of the piles in a LaTeX table.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2023, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@gmail.com"

import sys
import os
import json
import csv
from tabulate import tabulate
import logging

# Read the results on the piles.
pileResultsFileName= './piles_axial_force.json'

if os.path.isfile(pileResultsFileName):
    with open(pileResultsFileName,'r') as f:# Open JSON file
        pilesNdict= json.load(f)
else:
    logging.warning("file: '"+str(pileResultsFileName)+"' not found.")  

# Extract data to include in LaTeX table and drawings
latexDataRows= list()
dwgDataRows= [['COORDENADAS CIMENTACION PILOTES'], ['PILOTE', 'X', 'Y', 'TIPO']]
for key in dict(sorted(pilesNdict.items())):
    pileData= pilesNdict[key]
    pileType= pileData['soilType']
    (slsNmin, slsCF, slsWorstComb)= pileData['SLSNmin']
    (ulsNmin, ulsCF, ulsWorstComb)= pileData['ULSNmin']
    latexRow= [key, pileType[1:], slsNmin/1e3, slsCF, slsWorstComb, ulsNmin/1e3, ulsCF, ulsWorstComb]
    latexDataRows.append(latexRow)
    position= pileData['position']
    dwgDataRows.append([key, position[0]+440e3, position[1]+4.46e6, pileType[1:]])


# Create LaTeX output
csvFileName= './pile_coordinates.csv'
with open(csvFileName, 'w') as csvfile:
    writer = csv.writer(csvfile)
    for row in dwgDataRows:
        writer.writerow(row)
    
# print(tabulate(latexDataRows))


tableBegin= '''
\\topcaption{#tableTitle#} \\label{#tableLabel#}
\\tablefirsthead{\\hline \\multicolumn{8}{|c|}{#tableTitle#} \\\\
\hline
       &      & \\multicolumn{3}{|c|}{ELS} & \\multicolumn{3}{c|}{ELU}\\\\
\hline
Pilote & Tipo & $N_{min}\ (kN)$ & CF & Comb. &  $N_{min}\ (kN)$ & CF & Comb.\\\\
\hline
}
\\tablehead{\hline
       &      & \\multicolumn{3}{|c|}{ELS} & \\multicolumn{3}{c|}{ELU}\\\\
\hline
Pilote & Tipo & $N_{min}\ (kN)$ & CF & Comb. &  $N_{min}\ (kN)$ & CF & Comb.\\\\
\hline
}
\\tabletail{\\hline 
\\multicolumn{8}{r}{\emph{#continuesMsg#}} \\\\
}
\\tablelasttail{\\hline 
}

\\begin{center}
\\begin{supertabular}{|c|c|rrr|rrr|}
'''

tableEnd= '''
\\end{supertabular}
\\end{center}
'''
tableTitle= 'Minimum axial load in piles'
tableLabel= 'tb_maximum_pile_loads'
continuesMsg= 'Continued on next column'

tableBegin= tableBegin.replace('#tableTitle#', tableTitle)
tableBegin= tableBegin.replace('#tableLabel#', tableLabel)
tableBegin= tableBegin.replace('#continuesMsg#', continuesMsg)

texFileName= './piles_axial_force_supertabular.tex'

with open(texFileName, 'w') as texF:
    texF.write(tableBegin)
    for row in latexDataRows:
        pileId= row[0]
        outputStr= pileId
        outputStr+= ' & '+row[1]
        NminELS= format(row[2], ".2f") #str(round(row[2],2))
        outputStr+= ' & '+ NminELS
        elsCF= format(row[3], ".2f")
        outputStr+= ' & '+ elsCF
        #NmaxELS=round(dct[pil]['NmaxELS']*1e-3,2)
        outputStr+= ' & '+ row[4] # worst ELS combination.
        NminELU= format(row[5], ".2f")
        outputStr+= ' & '+ NminELU
        #NmaxELU=round(dct[pil]['NmaxELU']*1e-3,2)
        eluCF= format(row[6], ".2f")
        outputStr+= ' & '+ eluCF
        outputStr+= ' & '+ row[7] # worst ELU combination.
        outputStr+='\\\\\n'
        texF.write(outputStr)
    texF.write(tableEnd)
         
