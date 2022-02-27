# implementing a doubly linked list 
# printing forward and backwards the linked list

from os import preadv
from unittest import result


class Node:
    def __init__(self,data = None, next = None, prev = None):
        self.data = data
        self.prev = prev # prev = prev = previous node
        self.next = next # next = next node

class LinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head == None:
            print("this is an empty linked list")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr = llstr + str(itr.data) + ' ' '<-->' + ' '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        prev = None

        # reversing the pointers of the linked list
        while (itr != None):
            next = itr.next
            itr.next = prev
            prev = itr
            itr = next
        self.head = prev # making the last element the head
            
        # printing the new linked list with pointers reversed
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
            print ("-->")
    
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data,None)
            return

        itr = self.head
        
        while itr.next:
            itr = itr.next
            

        itr.next = Node(data,None)
            

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data) 

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([1,2,3,4,5])
    ll.print_forward()
    ll.print_backward()


    
