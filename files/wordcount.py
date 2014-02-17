f=open('a.txt','rU')
e=f.read().split()

  
wordcount={}
for i in e:
 if i not in wordcount:
    wordcount[i]=1
 else:
    wordcount[i]+=1
print wordcount
   








 

