def pall():
    c=[]
    for i in range(100,1000):
        for j in range(100,1000):
             k=i*j
             if  str(k)==str(k)[::-1]:
                 c.append((k,i,j))
     
    return max(c)
print pall()

