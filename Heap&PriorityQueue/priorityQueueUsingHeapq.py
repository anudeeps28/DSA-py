import heapq

# (priority, value)
list1 = [(1, "ria"),  (4, "sia"), (3, "gia")]
print(list1)

# because it is a min heap, the smaller value has more priority
# hence it will be removed first

heapq.heapify(list1)
print(list1)

print("###")

for i in range(len(list1)):
    print(heapq.heappop(list1))