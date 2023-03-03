class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None # points to the first node

    # append adds a new node to the end of the list
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # returns the list of values in the linked list
    def to_list(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.value)
            current_node = current_node.next
        return nodes
