import csv
cStr = '"aaaa","bbbb","ccc,ddd"'
newStr = [ '"{}"'.format(x) for x in list(csv.reader([cStr], delimiter=',', quotechar='"'))[0] ]
print(newStr)


