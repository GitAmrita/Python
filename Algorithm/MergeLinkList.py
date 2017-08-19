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
            self.tail = new_node

    def remove_current_node(self, node):
        if self.head == node:
            self.head = self.head.next
        else:
            curr_node = self.head.next
            prev_node = self.head
            while curr_node is not None:
                if curr_node == node:
                    if curr_node == self.tail:
                        self.tail = prev_node
                    prev_node.next = curr_node.next
                    break
                curr_node = curr_node.next
                prev_node = prev_node.next
        return node

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print ('The value at the node is {}'.format(curr_node.data))
            curr_node = curr_node.next


class MergeLists:
    def __init__(self, l1, l2):
        self.current1 = l1.head
        self.current2 = l2.head

    def merge_lists(self):
        while self.current1 is not None and self.current2 is not None:
            if self.current1.data < self.current2.data:
                l1.remove_current_node(self.current1)
                result.add_node_to_end(self.current1.data)
                self.current1 = self.current1.next
            elif self.current1.data > self.current2.data:
                l2.remove_current_node(self.current2)
                result.add_node_to_end(self.current2.data)
                self.current2 = self.current2.next
            else:
                l1.remove_current_node(self.current1)
                result.add_node_to_end(self.current1.data)
                l2.remove_current_node(self.current2)
                result.add_node_to_end(self.current2.data)
                self.current1 = self.current1.next
                self.current2 = self.current2.next
        while self.current1 is not None:
            l1.remove_current_node(self.current1)
            result.add_node_to_end(self.current1.data)
            self.current1 = self.current1.next
        while self.current2 is not None:
            l2.remove_current_node(self.current2)
            result.add_node_to_end(self.current2.data)
            self.current2 = self.current2.next
        return result


if __name__ == "__main__":
        l1 = LinkedList()
        l1.add_node_to_end(1)
        l1.add_node_to_end(2)
        l1.add_node_to_end(8)
        l1.add_node_to_end(9)
        l1.add_node_to_end(10)
        l1.add_node_to_end(11)
        l1.add_node_to_end(12)
        l1.add_node_to_end(15)
        l2 = LinkedList()
        l2.add_node_to_end(2)
        l2.add_node_to_end(5)
        l2.add_node_to_end(8)
        result = LinkedList()
        merge = MergeLists(l1, l2)
        result = merge.merge_lists()
        result.print_list()

