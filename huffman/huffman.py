codes={}
def frequency(str):
    freqs={}
    for ch in str:
        freqs[ch]=freqs.get(ch,0)+1
    return freqs
s=frequency("aaabccdeeeeeffg")

print s

def sortfreq(s):
    letters=s.keys()
    tuples=[]
    for let in letters:
       tuples.append((s[let],let))
    tuples.sort()
    return tuples 
tuples=sortfreq(s)
print tuples

def buildtree(tuples):
    while len(tuples)>1:
        leasttwo=tuple(tuples[0:2])
        rest=tuples[2:]
        combfreq=leasttwo[0][0]+leasttwo[1][0]
        tuples=rest+[(combfreq,leasttwo)]
        tuples.sort()
    return tuples[0]
tree= buildtree(tuples)
print tree

def trimtree(tree):
    p=tree[1]
    if type(p)==type(""):return p
    else:return (trimtree(p[0]),trimtree(p[1]))
trim=trimtree(tree)
print trim
def assigncodes(node,pat=''):
    global codes
    if type(node)==type(""):
        codes[node]=pat
    else:
        assigncodes(node[0], pat+"0")
        assigncodes(node[1], pat+"1")
assigncodes(trim)
print codes 
def encode(str):
    global codes
    output=""
    for ch in str:
     output+=codes[ch]
    return output
encoding= encode("aaabccdeeeeeffg")
print encoding
def decode(tree,str):
    output=""
    p=tree
    for bit in str:
        if bit=='0':p=p[0]
        else       :p=p[1]
        if type(p)==type(""):
            output+=p
            p=tree
    return output
print decode(trim,encoding)
