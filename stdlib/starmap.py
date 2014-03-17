from itertools import*
value=[(0,5),(1,5),(2,5),(3,5),(4,5)]
print 'Multiplication table of 5'
for i in starmap(lambda x,y:(x,y,x*y),value):
 
 print '%d * %d = %d'%i
