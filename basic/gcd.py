def gcd(a,b):
 
  while b!=0:
      r=b
      b=a%b
      a=r
       
        
  return r
print gcd(10,100)
