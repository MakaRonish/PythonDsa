# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        if head is None:
            return 0
        else:
            cur = head
            count = 1
            while cur.next is not None:
                count += 1
                cur = cur.next
            return count
