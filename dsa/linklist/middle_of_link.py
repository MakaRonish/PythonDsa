# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def count(self, head):
        if head is None:
            return 0
        cur = head
        c = 1
        while cur.next is not None:
            c += 1
            cur = cur.next
        return c

    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a = self.count(head)
        a = a // 2
        cur = head
        for i in range(a):
            cur = cur.next
        return cur
