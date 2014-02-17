def fer(a,b):
 i=a
 x=1
 if b==0:
  return 1

  while x<b:

   i=a*i
   x=x+1
   i=i-a 
   print i
   if i%a==0:
    print "fermat conditions satisfied"

print fer(2,3)















































 



























