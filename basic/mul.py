def mul(n):

    
   while n>0: 
        if n<10:
             a=n%10
    
        elif n<100:  
             b=n%100/10
             c=n%10
             a=b*c
 
        else:
             b=n/100
             c=n%100/10
             d=n%10
             a=b*d*c
   
    
   return a
print mul(1)
