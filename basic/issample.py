
def insert_into_sorted_list(a, x):
  for i in range(len(a)):
    if a[i]>x:
     a.insert(i,x)
     return a

def inssample(b):
    i=0
    c=[]
    c.append(b[i]) 
    while i<len(b):

     
     
     insert_into_sorted_list(c,b[i])
     i+=1        

 
    print c

               
                

inssample([23,19,12,3,11,2])


#print insert_into_sorted_list([10,23,4],6)
