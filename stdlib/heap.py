import heapq
def heaps(a):
       h=[]
       
       for i in a:
        heapq.heappush(h,i)
        print heapq.heappop(h)
        print heaps(h)
heaps([1,2,3,4,0])

