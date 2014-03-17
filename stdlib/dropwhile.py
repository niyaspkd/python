from itertools import*
def should_drop(x):
 print 'testing:',x
 return (x<1)
for i in dropwhile(should_drop,[-1,1,0,2,3]):
 print 'yielding',i 
