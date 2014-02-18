def prim(a):
 if a==1:
    return True
 i=2
 x=a**(0.5)
 while i<x:
    if a%i==0:
        break
    else:i+=1
 return a%i!=0


    


x=sum(filter(prim,range(2000000)))
print x
