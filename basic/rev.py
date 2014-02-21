def rev(n):
    d=0
    while n>0: 
      s=n%10+d
      d=(s*10)
      n=n/10
    return s
print rev(1234)
