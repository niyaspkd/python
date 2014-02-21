def div(n):
    c=[]
    for i in range(1,n):
        if n%i==0:
            c.append(i)
    return c 

print div(12)

def prime(n):
    s=div(n)
    if len(s)==1:
       print 'prime',n
  
prime(11)

