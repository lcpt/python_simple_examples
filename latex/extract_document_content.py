# -*- coding: utf-8 -*-
''' From a LaTeX document extract the text between \begin{document} and 
\end{document}.
'''

__author__= "Luis C. Pérez Tato (LCPT) and Ana Ortega (AO_O)"
__copyright__= "Copyright 2025, LCPT and AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es" "ana.Ortega@ciccp.es"

def get_latex_document_contents(inputFile):
    ''' From a LaTeX document extract the text between \begin{document} and 
        \end{document}.

    :param inputFile: file to extract the content from.
    '''    
    retval= str()
    readRetval= False
    with open(inputFile, 'r') as ltx_input:
        while line := ltx_input.readline():
            ln= line.rstrip()
            if('\\begin{document}' in ln):
                readRetval= True
            elif('\\end{document}' in ln):
                readRetval= False
            else:
                if(readRetval):
                    retval+= line
    return retval
            
contents= get_latex_document_contents(inputFile= './sample_document.tex')
with open('./document_content.tex', 'w') as ltx_output:
    ltx_output.write(contents)

