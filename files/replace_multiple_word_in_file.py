f1 = open('file1.txt', 'r')
f2 = open('file2.txt', 'w')

checkWords = ("old_text1","old_text2","old_text3","old_text4")
repWords = ("new_text1","new_text2","new_text3","new_text4")

for line in f1:
    for check, rep in zip(checkWords, repWords):
        line = line.replace(check, rep)
    f2.write(line)
f1.close()
f2.close()

 
