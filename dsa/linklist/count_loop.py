# User function Template for python3

"""
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

"""


class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        # Your code here
        cur = head
        data = set()
        while cur is not None:
            if cur in data:
                loop = cur.next
                count = 1
                while loop != cur:
                    count += 1
                    loop = loop.next
                return count
            data.add(cur)
            cur = cur.next
        return 0
