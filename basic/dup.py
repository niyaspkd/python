def dup(l):
 s=[]
 c=0
 for i in range(len(l)):
  if l[i] in l[i+1:] and l[i] not in s:
   s.append(l[i])


 return s
print dup([1,2,1,3,1,2,5])
