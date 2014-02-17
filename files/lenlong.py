c=[]
f=open('lovestory.txt','rU')
e=f.readlines()

for i in e:
 c.append(len(i))
print max(c)

