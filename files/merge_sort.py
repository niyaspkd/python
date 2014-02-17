def merge(a,b):
 j=0
 i=0
 c=[]
 while i<len(a):
  if j<len(b):

   if a[i]<b[j]:
   
    c.append(a[i])
    i+=1
   else:
    c.append(b[j])
    j+=1
 while j<len(b):
  c.append(b[j])
  j+=1
  return c
 while i<len(a):
  c.append(a[i])
  j+=1
  return c
print merge([1,5,7,10],[2,8,9])













