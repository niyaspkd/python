def merge(a,b):
    l = []
    while a and b:
        if a[0] < b[0]:
            l.append(a.pop(0))
        else:
            l.append(b.pop(0))
    return l + a + b
#print merge([1,3,5],[2,4,9,10])

f1=open('numbers.txt','rU')
f2=open('numbers1.txt','rU')
e=f1.readlines()
e1=f2.readlines()
g=merge(e,e1)






 
