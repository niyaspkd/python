def max(a):
 for i in range(len(a)):
  for j in range(i+1,len(a)):
   if a[j]<a[i]:
    a[i],a[j]=a[j],a[i]
  return a[j]
 


 


print max([3,2,5,4])



