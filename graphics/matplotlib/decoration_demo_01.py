# -*- coding: utf-8 -*-
'''Decoration demo.'''

import math
import matplotlib.pyplot as plt

def i_m(i, T):
    return math.pow(1+i, T)*i/(math.pow(1+i, T)-1) - 1/T

i= 9/100.0

tRange= range(1,20)
values= list()
for T in tRange:
    values.append(i_m(i, T))

fig, ax = plt.subplots()
ax.plot(tRange,values)
plt.title("Average interest rate ($i_m$).")
plt.xlabel('T (years)', fontweight='bold')
plt.ylabel('Interest rate', style='italic')
plt.show()
