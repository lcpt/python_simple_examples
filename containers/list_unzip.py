# Python3 code to demonstrate
# Unzip a list of tuples
# using zip() and * operator

from __future__ import print_function


source_list = [('1','a'),('2','b'),('3','c'),('4','d')]
list1, list2 = zip(*source_list)

print("source list : " + str(source_list))
 
print("Modified lists are : " + str(list1)+' '+str(list2))
