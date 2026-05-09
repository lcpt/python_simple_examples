# -*- coding: utf-8 -*-
''' tkinter demo. A binary module that contains the low-level interface to Tcl/Tk.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2023, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

import tkinter as tk

window= tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
window.mainloop()

