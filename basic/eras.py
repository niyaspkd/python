def erasprime(n):
    c=[]
    d=[]
    e=[]
    x=2
  
    d.append(x)         
    for j in range(x+1,n,2):
        d.append(j)
        for i in d:
          c.append(i*j)              
                    
    for k in d:
    
     if k not in c:
          e.append(k)     
    return e 

            




    
print erasprime(300)
                         
