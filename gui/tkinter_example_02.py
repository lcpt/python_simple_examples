# -*- coding: utf-8 -*-
''' tkinter demo. A binary module that contains the low-level interface to Tcl/Tk.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2025, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

from tkinter import Tk
from tkinter import messagebox

root = Tk().withdraw()  # hide the root window

messagebox.showinfo('hello', 'world')  # show the messagebox
