import math
def sine(a,x):
    sine=0   
    for i in range(x):
     sign=(-1)**i
     sine=sine+((a**2.0*i+1)/math.factorial(2.0*i+1))*sign
    print sine
sine(0,10)
               
     
     
             
       
  

