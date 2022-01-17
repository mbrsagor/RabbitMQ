class Node(object):
    """Represent a Node in a linked list."""

    def __init__(self, item):
        self.data = item
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkList(object):
    """Represent a single link list"""

    def __init__(self):
        self.head = None

    def add(self, new_item):
        """create a new node with new_item and ads to to front"""
        node = Node(new_item)
        node.next = self.head
        self.head = node

    def __str__(self):
        """Return a string the represent all the node from the head in a list"""
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next
        return str(nodes)

    def delete(self, item):
        """Delete the target item/node from the link-list if exists"""

        if self.head.data == item:
            self.head = self.head.next
            return self.head

        prev = None
        current = self.head
        while current and current.data != item:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
        return self.head


link_list = LinkList()
link_list.add(10)
link_list.add(20)
link_list.add(30)
link_list.add(40)
link_list.add(50)

link_list.delete(20)
link_list.delete(50)
print(link_list)
