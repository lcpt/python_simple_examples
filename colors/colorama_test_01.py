# -*- coding: utf-8 -*-
''' colorama demo. Colorama makes ANSI escape character sequences (for producing colored terminal text and cursor positioning).'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2023, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

import colorama
from colorama import Fore, Back, Style

#Initialize colorama
colorama.init(autoreset=True)

#Print text using background and font colors
print(Back.RED + Fore.BLUE + "Welcome to LinuxHint")
#Add newline
print()
#Print text using background color
print(Back.GREEN + "I like programming")
