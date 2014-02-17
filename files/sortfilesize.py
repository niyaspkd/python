import os
d=[]
c=os.listdir('.')
for i in c:
 # print i,os.stat(i).st_size
   d.append((os.stat(i).st_size,i))


for u,v in sorted(d):
    print u,v
