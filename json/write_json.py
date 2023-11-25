# -*- coding: utf-8 -*-
''' Write json file. JSON (JavaScript Object Notation) is a lightweight data-interchange format.'''

__author__= "Luis C. Pérez Tato (LCPT) and Ana Ortega (AO_O)"
__copyright__= "Copyright 2022, LCPT and AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es ana.ortega@ciccp.es"

data= {'a list': [1, 42, 3.141, 1337, 'help', u'€'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42}}
import json
with open('write_json_output.json', 'w') as f:
    json.dump(data, f)
