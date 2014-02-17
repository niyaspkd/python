def binarytodict(n):
 c=[]
 while n>0:
  c.append(str(n%2))
  n=n/2
  
 return ''.join(c[::-1])




print {i:binarytodict(i) for i in range(101)}

