import pyparsing
# define a comma-separated-value as anything that is not a ','
csv_value = pyparsing.CharsNotIn(',')
cStr= u'strB, strB, "", "", "", "", "", strB, strB + " con conexión colateral", "", "", "","", strB, strB + " y dos feeders"'
tmp= pyparsing.delimitedList(csv_value).parseString(cStr).asList()

items= list()
for item in tmp:
    items.append(item.strip())

print(items)
