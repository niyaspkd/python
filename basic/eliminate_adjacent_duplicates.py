def eliminate_adjacent_duplicates(a):
  i=0
  while i<len(a):
   if a[i]==a[i-1]:
    a.pop(i)
    i-=1
   i+=1
  return a
print eliminate_adjacent_duplicates([1,2,2,3])




