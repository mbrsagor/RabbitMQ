class Node(object):
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


# Class for doubly Linked List
class DoublyLinkedList(object):
    def __init__(self):
        self.start_node = None

    # Insert Element to Empty list
    def insert_empty_list(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")

    # Insert element at the end
    def insert_to_end(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    # Delete the elements from the start
    def delete_at_start(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None

    # Delete the elements from the end
    def delete_at_end(self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

    # Traversing and Displaying each element of the list
    def display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")


# Create a new Doubly Linked List
NewDoublyLinkedList = DoublyLinkedList()
# Insert the element to empty list
NewDoublyLinkedList.insert_empty_list(10)
# Insert the element at the end
NewDoublyLinkedList.insert_to_end(20)
NewDoublyLinkedList.insert_to_end(30)
NewDoublyLinkedList.insert_to_end(40)
NewDoublyLinkedList.insert_to_end(50)
NewDoublyLinkedList.insert_to_end(60)
# Display Data
NewDoublyLinkedList.display()
# Delete elements from start
NewDoublyLinkedList.delete_at_start()
# Delete elements from end
NewDoublyLinkedList.delete_at_start()
# Display Data
NewDoublyLinkedList.display()
