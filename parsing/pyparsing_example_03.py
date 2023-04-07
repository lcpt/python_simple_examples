import pyparsing
# define a comma-separated-value as anything that is not a ','
csv_value = pyparsing.CharsNotIn(',')
result= pyparsing.delimitedList(csv_value).parseString("dkls,camión,lsdkjf,s12 34,@!#,213")
print(result)
