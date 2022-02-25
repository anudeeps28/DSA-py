class Node: #node class = represents an individual member of the linked list
    def __init__(self, data=None, next=None): #first argument = data, second argument = a pointer to the next element
        self.data = data # data can contain integers, text or complex objects
        self.next = next 

class LinkedList: 
    def __init__(self):
        self.head = None # head variable = points to the head of the linked list (the first element of the linked list)

    def print(self):
        if self.head is None: #head is blank = linklist is blank
            print("Linked list is empty")
            return

        itr = self.head # if not blank 
        llstr = ''

        while itr: # iterating through the linked list
            llstr += str(itr.data)+' --> ' # appending linked list items to llstr #if itr.next else str(itr.data)
            itr = itr.next

        print(llstr)

    def get_length(self): # ge the length of the linked list
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data): # taking data value and inserting at the beginning of the linked list
        node = Node(data, self.head) # creating node; # if you are adding something at the head position, the next item of this will be your previous head
        self.head = node # once you have done that, make the new head this new node

    def insert_at_end(self, data):
        if self.head is None: # linked list is empty
            self.head = Node(data, None) # new node created with next address None = NULL
            return

        itr = self.head #assigning the head values to a variable

        while itr.next: #iterating itr.next (loop goes till there is a value of itr.next)
            itr = itr.next #move to the next item

        itr.next = Node(data, None) #inserting at the last element

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: # you are at the element prior to the element that you want to insert at
                node = Node(data, itr.next) # creating a node whose next is previous element's next
                itr.next = node # new node is the next of previous next node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index): # remove an element at a given index
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next # pointing to the next element while removing the first
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: # we need to stop at the node prior to the one we want to remove
                itr.next = itr.next.next # skipping the element that we need to remove (pointing to next element's next)
                break  

            itr = itr.next
            count+=1

    def insert_values(self, data_list): # take a list of values and create a new fresh linked list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList() # creating linked list 
    ll.insert_at_begining(5)
    ll.insert_at_begining(89)
    ll.print()
    print(ll.get_length())  

    ll.remove_at(1)
    ll.print()

    ll.insert_values(["banana","mango","grapes","orange"]) 
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()