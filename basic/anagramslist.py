def anagrams(a,b):
    c=[]
    c.append(a)
    for j in range(len(b)):
            if sorted(a)==sorted(b[j]):
             c.append(b[j])
    return c  

#anagrams('eat',['man','tea','run','ate']) 

def anagramlist(a,b):
 e={}
 for i in a:
   d=anagrams(i,b)
   e[i]=d
   
 return e
print anagramlist(['eat','rat'],['ate','tea','art','tar','man']) 
