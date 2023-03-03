from linkedListClass import LinkedList

# traversing a linked list
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

current_node = linked_list.head
while current_node:
    print(current_node.value)
    current_node = current_node.next # Output: 1 2 3 4

# searching for a value in linked list
def search_linked_list(linked_list, value):
    current_node = linked_list.head
    while current_node:
        if current_node.value == value:
            return True
        current_node = current_node.next
    return False

print(search_linked_list(linked_list, 3)) # Output: True
print(search_linked_list(linked_list, 5)) # Output: False

# deleting a node from a linked list
def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next