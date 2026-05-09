import bisect 
a = [1, 2, 4, 5]
print('before: ', a)
retval= bisect.insort(a, 3) 
print('after: ', a)
print(retval)
