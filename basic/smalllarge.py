def smallarge(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j]<a[i]:
                a[i],a[j]=a[j],a[i]
    return(a[0],a[-1])    
  
      



        
            
            
print smallarge([5,6,3,7,10,9])


