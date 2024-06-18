# -*- coding: utf-8 -*-
''' Get LaTeX auxiliary file names from the name of the TeX file.'''

__author__= "Luis C. Pérez Tato (LCPT) and Ana Ortega (AO_O)"
__copyright__= "Copyright 2024, LCPT and AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es" "ana.Ortega@ciccp.es"

from pathlib import Path


latex_aux_extensions= ['.aux', '.log', '.out', 
                       '.bbl', '.blg', '.bcf', # Leftovers from bibtex
                       '.glg', '.gls', '.glo', # Leftovers from glossaries  
                       '.lof', '.lot', '.toc', # Remove leftovers from lists
                       '.mtc*', '.maf', # Remove leftovers from minitoc
                       '.run.xml', # Remove other stuff
                       '.acn', '.acr', '.alg', 
                       '.ist', '.synctex*', '.alg']

def get_latex_aux_posix_paths(texFileName):
    ''' Get LaTeX auxiliary file names from the given name.'''
    pth= Path(texFileName)
    retval= list()
    for ext in latex_aux_extensions:
        retval.append(pth.with_suffix(ext))
    return retval


print(get_latex_aux_posix_paths('test1.tex'))
print(get_latex_aux_posix_paths('tmp/test2.tex'))
                      
