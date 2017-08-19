class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def remove_duplicate(self):
        curr_node = self.head
        next_node = self.head.next
        while next_node is not None:
            if curr_node.data == next_node.data:
                curr_node.next = next_node.next
                next_node = next_node.next
            else:
                curr_node = curr_node.next
                next_node = next_node.next

    def print_list(self):
        curr = self.head
        while curr is not None:
            print ('{}'.format(curr.data))
            curr = curr.next


if __name__ == "__main__":
    l1 = LinkedList()
    l1.add_node_to_end(1)
    l1.add_node_to_end(2)
    l1.add_node_to_end(2)
    l1.add_node_to_end(2)
    l1.add_node_to_end(3)
    l1.add_node_to_end(3)
    l1.add_node_to_end(4)
    l1.add_node_to_end(5)
    l1.add_node_to_end(5)
    l1.remove_duplicate()
    l1.print_list()