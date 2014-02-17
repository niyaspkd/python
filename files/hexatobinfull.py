def binhexa(a):
    x=0
    b=reversed(a)
    print b
    n=0
    for i in b:
        if i>9:
                  
            if i=='A':
                x=x+10*(16**n)
            elif i=='B':
                x=x+11*(16**n)

            elif i=='C':
                x=x+12*(16**n)
            elif i=='D':
                x=x+13*(16**n)
            elif i=='E':
                x=x+14*(16**n)
            elif i=='F':
               x=x+15*(16**n)
               
        else:
            x=x+int(i)*(16**n)
        n += 1
               
    return x
    
print binhexa('FF')
