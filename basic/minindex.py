def min_index(a):
  	i=1
  	min_index=0
  	while i<len(a):
   		if a[i]<a[min_index]:
    			min_index=i
    		i += 1
    
  	print min_index
 
   
min_index([5,3,2,1])
