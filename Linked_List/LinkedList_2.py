from platform import node


class LinkedListNode:
    def __init__(self, value, NextNode):
        self.value = value
        self.NextNode = NextNode

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, value): #insert at the end of a list
        node = LinkedListNode(value)
        if self.head is none:
            self.head = node
            return

        currentNode = self.head
        while True:
            if currentNode.NextNode is None: #if there is no node after the current node
                currentNode.NextNode = node #we are going to make that next node our node
                break
            currentNode = currentNode.NextNode

    def PrintLinkedList(self):
        currentNode = self.head #getting the head
        while currentNode is not None: #simply traversing through the list
            print (currentNode.value, "->") #printing out the elements
            currentNode = currentNode.NextNode
        print ("None")

if __name__ =='__main__':
    ll = LinkedList()
    ll.PrintLinkedList()
    ll.insert ("3")
    ll.PrintLinkedList()
    ll.insert("44")
    ll.PrintLinkedList()
    ll.insert("55")
    ll.PrintLinkedList()


