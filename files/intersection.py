

f=open('lovestory.txt','rU')
f1=open('lovestory1.txt','rU')
for i in set(f)&set(f1):
 print i
