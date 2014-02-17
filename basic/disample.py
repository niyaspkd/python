def dicttolist(a):
    e=[]
    f=[]
    g=[]
    for i in a.values():
        e.append(i)
    for j in a.keys():
        f.append(j)
    for k in range(len(e)):
     g.append((f[k],e[k]))
    print g
dicttolist({'abc':20,'def':39,'efg':80})








