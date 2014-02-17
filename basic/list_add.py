def list_add(a,b):
 i=0
 while i<len(b):



  if len(a)==len(b):
   a[i]=a[i]+b[i]
   i+=1
 return a

print list_add([1,2,3],[2,3,4])


