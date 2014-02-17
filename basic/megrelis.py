def mergelis(a,b):
    c=[]
    i=0
    j=0
    while i<len(a):
        if j<len(b):
            if a[i]<b[j]:
                c.append(a[i])
                i+=1
            else:
                c.append(b[j])
                j+=1  
        
    while j<len(b):
        c.append(b[j])
        j+=1
    while i<len(a):
        c.append(a[i])
        j+=1
    print c





mergelis([1,2,3,7],[4,5,8])
