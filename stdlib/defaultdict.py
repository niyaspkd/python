import collections
s=[('yellow',1),('blue',2),('red',1),('blue',3),('red',4)]
d=collections.defaultdict(list)
for k,v in s:
 d[k].append(v)
print list(d.items())

