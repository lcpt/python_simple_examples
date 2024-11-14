from operator import itemgetter

L=[[0, 1, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
sortedList= sorted(L, key=itemgetter(2))
print(sortedList)
