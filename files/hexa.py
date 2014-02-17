def binarytodict(n):
    c=[]
    
    while n>0:
       
        n=n/16
        
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
         return x,n       


  


print binarytodict(10)






