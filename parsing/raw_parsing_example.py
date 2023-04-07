
testString= u'strB, strB, "", "", "", "", "", strB, strB + " con conexión colateral", "", "", "","", strB, strB + " y dos feeders", dkls,camión,"lsdkjf,abd",s12 34,@!#,213'

def parse_comma_separated_list(inputString, delimiter= ',', quotationMark= '"'):
    retval= list()
    item= str()
    quotedString= False
    for c in inputString:
        if(c==quotationMark):
            item+= c
            if(not quotedString): # Quoted string starts.
                quotedString= True
            else: # Quoted string ends.
                quotedString= False
        else:
            if(c==delimiter and not quotedString): # item ends.
                retval.append(item)
                item= str()
            else:
                item+=c
    retval.append(item)
    return retval

items1= parse_comma_separated_list(testString)
items2= parse_comma_separated_list("Según R.D. 773/97 y R.D. 1407/92. Equipo de Protección Individual (EPI) con marcado de conformidad CE.")

print(items1)
print(items2)

