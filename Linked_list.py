#learning python linkedlist

class LinkedListNode: #node class with 2 class members: data and next
    #node is a type of data structure
    def __init__(self, value, nextNode=None): #this is defining attributes
        self.value = value #data can contain information
        self.nextNode = nextNode #pointer to the next element/node

# 3 -> 7 -> 10
node1 = LinkedListNode("3")
node2 = LinkedListNode("7")
node3 = LinkedListNode("10")
node4 = LinkedListNode("77")
#connecting nodes
node1.nextNode = node2 #node1 -> node2 = "3" -> "7"
node2.nextNode = node3 #node2 -> node3 = "7" -> "10"
node3.nextNode = node4
#node1 -> node 2 -> node3

currentNode = node1
while True:
    print (currentNode.value, "->")
    if currentNode.nextNode is None: #making sure the current node is not the tail node
        print ("None")
        break
    currentNode = currentNode.nextNode

# class LinkedList: #2nd class
#     def __init__(self):
#         self.head = None #head variable points to the head of the linklist

#     def print_func(self): #this is a method to print
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
#             itr = itr.next
#         print(llstr)

#     def get_length(self): #this is the method to get length
#         count = 0 
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next

#         return count

#     def insert_at_begining(self, data): #method to insert at the beginning of the linklist
#         node = Node(data, self.head)
#         self.head = node

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return

#         itr = self.head

#         while itr.next:
#             itr = itr.next

#         itr.next = Node(data, None)

#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.insert_at_begining(data)
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break

#             itr = itr.next
#             count += 1

#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.head = self.head.next
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break

#             itr = itr.next
#             count+=1

#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)

#     def insert_after_value(self, data_after, data_to_insert):
#     # Search for first occurance of data_after value in linked list
#         x = ""
#         count = 0
#         itr = self.head
#         while itr:
#             if x == data_after:
#                 node = Node(dat a_to_insert,itr.next)
#                 itr.next = node
#             itr = itr.next
#             count += 1

# #this is an edit
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print_func()
#     #ll.insert_at(2,"apple")
#     #ll.print_func()
#     #ll.remove_at(2)
#     #ll.print_func()
#     ll.insert_after_value("mango","apple")
#     ll.print_func()


#     #ll.insert_values([45,7,12,567,99])
#     #ll.insert_at_end(67)
#     #ll.print_func()
