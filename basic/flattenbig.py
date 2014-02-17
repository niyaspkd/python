def flatten(a,c=[]):
    for x in a:
        if isinstance(x,list):
          flatten(x,c) 
        else:
            c.append(x)
    return c

print flatten([[[[1]]]])
