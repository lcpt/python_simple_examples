# -*- coding: utf-8 -*-
''' Simple example that shows how to create an spreadsheet book.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2023, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

from collections import OrderedDict
import pyexcel as pe

a_dictionary_of_two_dimensional_arrays = {
         'Sheet 1':
             [
                 [1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0],
                 [7.0, 8.0, 9.0]
             ],
         'Sheet 2':
             [
                 ['X', 'Y', 'Z'],
                 [1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0]
             ],
         'Sheet 3':
             [
                 ['O', 'P', 'Q'],
                 [3.0, 2.0, 1.0],
                 [4.0, 3.0, 2.0]
             ]
     }
data = OrderedDict()
data.update({"Sheet 2": a_dictionary_of_two_dimensional_arrays['Sheet 2']})
data.update({"Sheet 1": a_dictionary_of_two_dimensional_arrays['Sheet 1']})
data.update({"Sheet 3": a_dictionary_of_two_dimensional_arrays['Sheet 3']})
pe.save_book_as(bookdict=data, dest_file_name="book.ods")
