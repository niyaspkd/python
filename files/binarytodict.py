def hexatodict(n):
     c=[]

     while n>0:
         if n%16==10:
             c.append('A')
         elif n%16==11:
             c.append('B')
         elif n%16==12:
             c.append('C')
         elif n%16==13:
             c.append('D')
         elif n%16==14:
             c.append('E')
         elif n%16==15:
           c.append('F')

         else:
           c.append(str(n%16))
         n=n/16
        
           
             
     return ''.join(c[::-1])
                  
          
print hexatodict(65535)




