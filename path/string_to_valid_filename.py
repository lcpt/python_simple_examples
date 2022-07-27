s= 'foo-bar#baz?qux@127/\\9]'
filename= "".join(x for x in s if x.isalnum())
print(filename)

