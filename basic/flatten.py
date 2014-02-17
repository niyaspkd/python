def flatten(a):
    c=[]
    for x in a:
        if isinstance(x,list):
            for i in x:
                c.append(i)
        else:
            c.append(x)
    return c

print flatten([1,2,[3,4],[5,6]])
