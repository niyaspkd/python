def merge(a,b):
 j=0
 i=0
 c=[]
 while i<len(a) and j<len(b):
  if j<len(b):

   if a[i]<b[j]:
   
    c.append(a[i])
    i+=1
   else:
    c.append(b[j])
    j+=1
 while i<len(a):
   c.append(a[i])
   i+=1
 return c

 while j<len(b):
  c.append(b[j])
  j+=1
 return c
   
#print merge([1,3,5,7,9,13],[2,8,12])

f=open('numbers.txt','rU')
f1=open('numbers1.txt','rU')
e=f.readlines()
e1=f1.readlines()


g=[x.strip() for x in e]
g1=[y.strip() for y in e1]
g.pop()
g1.pop()

s=map(int,g)
t=map(int,g1)

                                

for k in merge(s,t) :
  print k














