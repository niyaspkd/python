def pyth():

   for i in range(1,1000):
    for j in range(i,1000):
     c=1000-i-j
     if c>0:
        if c*c==i*i+j*j:
         return i*j*c ,i,j,c
         


print pyth()
