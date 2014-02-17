def inserted_into_sorted(a,b):
  for i in range(len(a)):
      if a[i]>b:
         a.insert(i,b)
         return a

print inserted_into_sorted([10,26,32,40],9)

