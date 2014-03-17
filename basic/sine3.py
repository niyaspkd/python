import math



def sine(x):
    n = 0
    sine = 0
    t=(-1)**(n)*(x**(2*n+1))/(math.factorial(2*n+1))
    while math.fabs(t)>1.0e-6:
        sine=sine+t        
        n+= 1
        t= (-1)**(n)*(x**(2*n+1))/(math.factorial(2*n+1))
    return sine

print sine(math.pi)
