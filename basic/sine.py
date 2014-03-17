
def fact(n):
 
 sum=1
 for num in range(n):
   num=num+1
   sum=num*sum
 return sum
def sine(a):
    sine=0   
    n=0
    x=2*n+1
    sign=(-1)**n  
    while n<100:
        sine=sine+(sign)*((a**x)/fact(x))
            
        n+=1  
        print sine
print sine(0.1)


               
       
  

