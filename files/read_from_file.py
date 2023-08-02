# Read lines from file

file= open('./test.txt', 'r')
lines= file.readlines()

for l in lines:
    print(l.strip())

print('read ', len(l), ' lines of text.')
