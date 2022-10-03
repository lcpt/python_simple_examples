# -*- coding: utf-8 -*-
''' Get the symbols from a module.'''

from postprocess import control_vars

def getImportedNames (module):
    names = module.__all__ if hasattr(module, '__all__') else dir(module)
    return [name for name in names if not name.startswith('_')]

print(getImportedNames(control_vars))
