from operator import itemgetter

test= ([20, 10], [10, 74])
# raw maximum.
mx1= max(test)
# item getter
mx2= max(test, key= itemgetter(1))
mx3= max(max(test, key= itemgetter(0))[0], max(test, key= itemgetter(1))[1])

print(mx1)
print(mx2)
print(mx3)
