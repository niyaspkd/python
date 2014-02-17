def anagrams(a,b):
    c=[]
    c.append(a)
    for j in range(len(b)):
            if sorted(a)==sorted(b[j]):
             c.append(b[j])
    print c  

anagrams('eat',['man','tea','run','ate']) 


def all_anagram(a)
 d=[]
 
