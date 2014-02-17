'123'

#'321'

#sum = 0

#sum <- 3 * 16**0 + previous valu

#sum <- 2 * 16**1 + previous value

#sum <- 1 * 16**2 + previous value



def sum(a):
    b=reversed(a)
    sum=0 
    n=0
    for i in b:   
        
         sum=sum+int(i)*(16**n)
         n+=1
    return sum       
        
        
print sum('16')




