import sys
c=[]
f=open('lovestory.txt','rU')
e=f.readlines()
for i in e:
   e=len(i)
   c.append(i)
   print max(c)
   print min(c)

