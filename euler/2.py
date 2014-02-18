def fib(n):
    c=[]
    d=[]
    a,b=0,1
    c.append(a)
    while b<n:
        c.append(b)
        a,b=b,a+b
    for i in c:
     if i%2==0:
       d.append(i)
    return sum(d)


print fib(4000000)
        
