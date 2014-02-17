def has_duplicates(a):

  for i in range(len(a)):
   if a[i] in a[i+1:]:
    print True

 


has_duplicates([1,4444,3,1])
