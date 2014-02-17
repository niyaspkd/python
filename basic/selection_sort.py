def selectionsort(a):
 for index in range(0,len(a)):
  min=index
  for j in range(index+1,len(a)):
   if a[j]<a[min]:
      min=j
  a[index],a[min]=a[min],a[index]
 return a


print selectionsort([4,3,2,1])
     

