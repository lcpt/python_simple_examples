# -*- coding: utf-8 -*-
''' Simple example that shows how to read/write from an Excel file.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2023, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

import pyexcel as pe

sheet = pe.get_sheet(file_name="example.ods")
sheet.row += [12, 11, 10]
sheet.save_as("new_example.ods")
pe.get_sheet(file_name="new_example.ods")
