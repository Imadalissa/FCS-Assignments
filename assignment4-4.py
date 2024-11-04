class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def deleteAtLocation(self, location):
        if self.head is None:
            return

        # If the location is 0, delete the head node
        if location == 0:
            self.head = self.head.next
            return

        # Traverse to the node before the one to be deleted
        current_node = self.head
        for i in range(location - 1):
            if current_node.next is None:
                return  # Location is out of range
            current_node = current_node.next

        # Delete the node
        if current_node.next is None:
            return  # Location is out of range
        next_node = current_node.next.next
        current_node.next = next_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage
linked_list = LinkedList()
linked_list.append(12)
linked_list.append(56)
linked_list.append(76)
linked_list.append(11)
linked_list.append(0)

print("Original Linked List:")
linked_list.print_list()

# Delete the head node (location 0)
linked_list.deleteAtLocation(0)
print("Linked List after deleting the head node (location 0):")
linked_list.print_list()

# Delete the node at location 3 (containing 11)
linked_list.deleteAtLocation(3)
print("Linked List after deleting the node at location 3:")
linked_list.print_list()