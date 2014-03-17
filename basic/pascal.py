def sumFirstTwo(lis):
    outlis = [lis[0]]
    for i in range(len(lis)): 
     a=sum(lis[i:i+2]) 
     outlis.append(a)
    return outlis
#print sumFirstTwo([1,4,6,6,1])


def pyramid(a):
    i=len(a)
    print a
    while i<7:
  
     a=sumFirstTwo(a)
     print a
     i+=1
  
pyramid([1,2,1])

