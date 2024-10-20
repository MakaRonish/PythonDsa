class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def searchKey(self, n, head, key):
        if head is None:
            return False
        else:
            cur = head
            for i in range(n):
                if cur.data == key:
                    return True
                else:
                    cur = cur.next
            return False
        # Code here
