# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def constructLL(self, arr):
        for i in range(len(arr)):
            new_node = Node(arr[i])
            if self.head is None:
                self.head = new_node
            else:
                cur = self.head
                while cur.next is not None:
                    cur = cur.next
                cur.next = new_node
        return self.head


# faster
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.head = None
        self.tail = None

    def constructLL(self, arr):
        for i in range(len(arr)):
            new_node = Node(arr[i])
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
        return self.head
