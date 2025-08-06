# -*- coding: utf-8 -*-
''' Simple example that shows how to read from an Excel file.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2025, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

from openpyxl import load_workbook
workbook = load_workbook(filename="xls_example.xlsx")

sheet = workbook[workbook.sheetnames[0]]
for row in sheet.iter_rows():
    lc= row[0].value
    if(lc):
        is_load_combination= isinstance(lc, int)
        print(lc, is_load_combination)
