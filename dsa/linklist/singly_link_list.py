class node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class SinglyLInkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if self.head is None:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val)
                current = current.next

    def insertHead(self, val):
        new_node = node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, val, index):
        new_node = node(val)
        if index == 0 or self.head is None:
            self.insertHead(val)
        else:
            # my
            # c = 0
            # current = self.head
            # while c < index - 1 and current.next is not None:
            #     c += 1
            #     current = current.next
            # current.next, new_node.next = new_node, current.next

            # sir
            curr = self.head
            prev = None
            count = 0
            while count < index and curr.next is not None:
                prev = curr
                curr = curr.next
                count += 1
            new_node.next = curr
            prev.next = new_node

    def deleteHead(self):
        if self.head is None:
            print("cannot delete")
        else:
            cur = self.head
            self.head = cur.next

    def delete(self, val):
        cur = self.head
        prev = None
        while cur.val != val and cur.next is not None:
            prev = cur
            cur = cur.next
        if cur.val == val:
            self.deleteHead()
        elif prev.val == val:
            prev.next = cur.next
        else:
            print("not found")


s1 = SinglyLInkedList()

s1.append(1)
s1.append(2)
s1.append(3)
s1.append(4)
s1.append(9)
s1.insert(0, 0)
s1.insert(5, 5)
s1.traverse()
s1.delete(0)
print("----")
s1.deleteHead()
s1.traverse()

a = 3
b = 4
a = a ^ b
b = a ^ b
a = a ^ b
