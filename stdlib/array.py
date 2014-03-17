import array
import binascii
s='This is array'
a=array.array('c',s)
print 'as string' ,s
print 'as array'  ,a
print binascii.hexlify(a)
