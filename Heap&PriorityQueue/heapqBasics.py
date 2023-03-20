import heapq # in-built min - heap in python

# heappush - pushes into the array(heap) while maintaining heap property
heap = []
heapq.heappush(heap, 10)
print(heap)

heapq.heappush(heap, 1)
print(heap)

heapq.heappush(heap, 5)
print(heap)

# heappop - returns the smallest value (because it is min heap) while also deleting it from the heap
# all while maintining the heap property
print(heapq.heappop(heap))
print(heap)

print(heapq.heappop(heap))
print(heap)

# heapify - converts the given list to heap (binary heap)
myList = [1,3,4,2,5,4,6]
print(myList)
heapq.heapify(myList) # converts the array to heap
print(myList)

# heappushpop - first it pushes a new item while maintaining the heap property,
# after that it will return the smallest value from the heap while maintaining the heap property

print(heapq.heappushpop(myList, 89))
print(myList)

# heapreplace - pop the smallest element and then insert the new element
# this is the reverse of heappushpop
print(heapq.heapreplace(myList, 100))
print(myList)


# nsmallest - this will return n smallest numbers in the given iterable
mylist2 = [1,20,5,4,3,6,2] # this is not a binary heap, still it works
print(heapq.nsmallest(2, mylist2))

heapq.heapify(mylist2)
print(heapq.nsmallest(2, mylist2)) # every after heapify it gives

# nlargest - it gives n largest numbers in the iterable
print(heapq.nlargest(3, mylist2))

