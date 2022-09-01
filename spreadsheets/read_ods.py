# -*- coding: utf-8 -*-
''' Simple example that shows how to read/write from an Excel file.'''

import pyexcel as pe

sheet = pe.get_sheet(file_name="example.ods")
sheet.row += [12, 11, 10]
sheet.save_as("new_example.ods")
pe.get_sheet(file_name="new_example.ods")
