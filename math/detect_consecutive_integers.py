# -*- coding: utf-8 -*-
''' Find runs of consecutive numbers using groupby.  The key to the solution
    is differencing with a range so that consecutive numbers all appear in
    same group.
'''

from operator import itemgetter
from itertools import groupby

data = [ 1,  4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
for k, g in groupby(enumerate(data), lambda ix : ix[0] - ix[1]):
    print(list(map(itemgetter(1), g)))
