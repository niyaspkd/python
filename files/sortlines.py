c=[]
f=open('lovestory.txt','rU')
e=f.readlines()

for i in e:  
 c.append((len(i),i))
c=sorted(c)
for u,v in c:
  print u,v

   
 


