def su(a):
 s=[a[i:i+2] for i in range(0,len(a),2)]
 d=[sum(b) for b in s]
 return d  
print su([1,2,3,4,5,6])
