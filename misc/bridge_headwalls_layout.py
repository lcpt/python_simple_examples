# -*- coding: utf-8 -*-

# Underpass headwalls layout as described in:
# Ponts-cadres et portiques
# Guide de conception
# Service d'Études Techniques des Routes et Autoroutes (SETRA)
# Décembre 1992
# Page 30

import math

L= 10.0#10.75
phi= math.radians(90.0) #Bridge skew angle.

alpha= math.radians(15+0.03 * L**2)
sinAlpha= math.sin(alpha)
cosAlpha= math.cos(alpha)
tgPhi= math.tan(phi)
#The expression in the book is incorrect use this:
beta= math.atan2(sinAlpha*tgPhi,(tgPhi*cosAlpha-2*sinAlpha))

print 'alpha= ', math.degrees(alpha)
print 'beta= ', math.degrees(beta)



