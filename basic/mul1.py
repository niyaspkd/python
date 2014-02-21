def mul1(n):
    s=1
    while n>0:
        s*=n%10
        n=n/10
    return s
print mul1(1234)

