# -*- coding: utf-8 -*-

import re

testExpr= re.compile('ab*')

wordList= ['printer', 'second', 'library', 'absolute', 'receiving', 'match', 'absurd', 'pattern', 'recognition', 'abbey']

matchingWords= list()
for word in wordList:
    result= testExpr.match(word)
    if not result is None:
        matchingWords.append(word)

print('matching words: ', matchingWords)
