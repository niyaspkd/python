def merge(a,b):
 c=[]
 
 for x in a:
  for y in b:
   if a.index(x)==b.index(y):
  
     c.append(x)
     c.append(y)
 print c
merge([1,3,20],[5,11,25,30])

