def dicttolist(a):
    
    f=[]
   
    for j in a.values():

     for i in a.keys():
        f.append((i,j))
     return f
print dicttolist({'abc':20,'def':39,'efg':80})








