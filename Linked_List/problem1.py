# code to add and remove a linked list node by value (not by index)
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' # if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    
    

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None: # linked list is empty
            print("Linked List is empty")

        if self.head.data == data_after: # value after which we want to add is the first node
            self.head.next = Node(data_to_insert,itr.next)
        
        itr = self.head # the values after which we want to add comes somewhere in between
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break

            itr = itr.next
            
    def remove_by_value(self, data):     # Remove first node that contains data
        if self.head == None: # if the linked list is empty
            return

        if self.head.data == data: # if value to be removed is in the first node 
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
                
            itr = itr.next

    


        

if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_values([7,9,12,17,18])
    ll.print()

    ll.insert_after_value(12,16)
    ll.print()

    ll.remove_by_value(17)
    ll.print()
