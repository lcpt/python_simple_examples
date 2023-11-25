# -*- coding: utf-8 -*-
''' colorama demo. Colorama makes ANSI escape character sequences (for producing colored terminal text and cursor positioning).'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2023, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

#Import required modules
from colorama import Fore
from colorama import Style

okString= Fore.GREEN+'OK'+Style.RESET_ALL
koString= Fore.RED+'KO'+Style.RESET_ALL

#Print text using background and font colors
print('OK string: ',okString)
print('KO string: ',koString)

