#! /usr/bin/env python
# -*- coding: utf-8 -*-

import locale

value = 123456789
localeStrings= ['', 'en_US.utf-8', 'en_US', 'es_ES.utf-8']

for ls in localeStrings:
    l= locale.setlocale(locale.LC_ALL, ls)
    s= locale.currency(value, grouping=True, symbol= True)
    print(ls, s)


