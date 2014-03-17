import string
d=string.maketrans('abc','134')
s= 'hi abc'
print s.translate(d)
