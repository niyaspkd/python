def maxdup(a):
 d=[]
 b=set(a)
 for i in b: 
   c=a.count(i)
   d.append(c)
      
 return sorted(d)[-1]
   
  
 
 

print maxdup([1,2,3,2,2, 2,2,1])

