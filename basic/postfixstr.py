def postfix(a):
 a=a.split()
 
 c=[]
 for x in a: 
  if x=='+':
   e=c.pop()
   f=c.pop()
   c.append(e+f)
  elif x=='*':
   e=c.pop()
   f=c.pop()
   c.append(e+f)
  else:
    x=int(x) 
    c.append(x)
 print c[0]



postfix('1 2 3 + *')
