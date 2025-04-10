# -*- coding: utf-8 -*-
''' Get a Unicode string from a LaTeX string.'''

__author__= "Luis C. Pérez Tato (LCPT) and Ana Ortega (AO_O)"
__copyright__= "Copyright 2024, LCPT and AO_O"
__license__= "GPL"
__version__= "3.0"
__email__= "l.pereztato@ciccp.es" "ana.Ortega@ciccp.es"

import flatlatex

c= flatlatex.converter()


print(c.convert('\epsilon_{xx}'))
print(c.convert('\sigma_{xx}'))
print(c.convert('\sigma_{zz}'))
print(c.convert('\sigma_{33}'))
