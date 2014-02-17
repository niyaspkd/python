def decimaltohexa(n):
    c=[]
    if n<10:
        print n 
    else:
        if n%16==10:
            x='A'
        elif n%16==11:
            x='B'
        elif n%16==12:
            x='C'
        elif n%16==13:
            x='D'
        elif n%16==14:
            x='E'
        elif n%16==15:
            x='F'
        else:
            x=n%16
    n=n/16  
    c.append((n,x))
    for u,v in  c:
          print u,v

  
  
   
  
k=decimaltohexa(17)
print k

