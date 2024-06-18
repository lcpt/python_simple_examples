# -*- coding: utf-8 -*-
''' Get a PDF file from a LaTeX string.'''

__author__= "Luis C. Pérez Tato (LCPT) and Ana Ortega (AO_O)"
__copyright__= "Copyright 2024, LCPT and AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es" "ana.Ortega@ciccp.es"

import os
import subprocess
from pathlib import Path


tex_string= r"""
\documentclass{article}

\begin{document}
Hello World
\end{document}
"""
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
  
def latex_string_to_pdf(outputFileName, showPDF= False, targetDir= './', tmpDir= '/tmp'):
    ''' Converts a LaTeX string into a PDF file.

    :param outputFileName: name of the PDF output file.
    :param showPdf: if true display the PDF file on the screen.
    '''
    output_directory_path= tmpDir
    outputFilePath= Path(outputFileName)
    outputBaseName= outputFilePath.stem
    outputFileName= output_directory_path+'/'+outputFileName

    # Write LaTeX file.
    with open(outputFileName, "w") as tex_file:
        tex_file.write(tex_string)

    # Run pdflatex
    output_directory_opt= '--output-directory='+output_directory_path
    subprocess.run(["pdflatex", output_directory_opt, outputFileName], stdout= subprocess.DEVNULL,  stderr=subprocess.STDOUT)
    subprocess.run(["pdflatex", output_directory_opt, outputFileName], stdout= subprocess.DEVNULL,  stderr=subprocess.STDOUT)
    subprocess.run(["pdflatex", output_directory_opt, outputFileName], stdout= subprocess.DEVNULL,  stderr=subprocess.STDOUT)
    # Remove auxiliary files.
    latex_aux_posix_paths= get_latex_aux_posix_paths(outputFileName)
    for pth in latex_aux_posix_paths:
        pth.unlink(missing_ok=True)
    # Move PDF file to target directory.
    pdf_pth= Path(output_directory_path+'/'+outputBaseName+'.pdf')
    target_pth= Path(targetDir+'/'+outputBaseName+'.pdf')
    pdf_pth.rename(target_pth)
    if(showPDF):
        filepath= str(target_pth)
        subprocess.run(('xdg-open', filepath))
    return filepath


pdfFile= latex_string_to_pdf(outputFileName= 'filename.tex', showPDF= True)
input("Press Enter to continue...")

if os.path.exists(pdfFile):
    os.remove(pdfFile)
