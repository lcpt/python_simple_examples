# -*- coding: utf-8 -*-
#! /usr/bin/env python
''' Set locale demo.'''

__author__= "Luis C. Pérez Tato (LCPT)"
__copyright__= "Copyright 2023, LCPT"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es"

import locale

value = 123456789
localeStrings= ['', 'en_US.utf-8', 'en_US', 'es_ES.utf-8']

for ls in localeStrings:
    l= locale.setlocale(locale.LC_ALL, ls)
    s= locale.currency(value, grouping=True, symbol= True)
    print(ls, s)


