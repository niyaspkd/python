def binarysearch(a,b):
    n=len(a)
    low=0
    high=n
    mid=(high+low)/2
    while low<high:
        
        if a[mid]<b:
            mid=mid+1

        elif a[mid]>b:
            mid=mid-1
        else:
            return a[mid]
print binarysearch([1,2,3,4,5],4)

