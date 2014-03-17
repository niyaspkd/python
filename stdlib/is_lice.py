from itertools import*
print 'stop at 5'
for i in islice(count(),5):
 print i
print 'stop at 10'
for i in islice(count(),5,10):
 print i
print 'stop at 100'
for i in islice(count(),0,100,10):
 print i
