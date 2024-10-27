# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def count(self, head):
        c = 0
        cur = head
        while cur:
            cur = cur.next
            c += 1
        return c

    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        if head.next is None:
            return

        c = self.count(head)
        if c == n:
            head = head.next
            return head
        cur = head
        for i in range(1, c - n):
            cur = cur.next
        cur.next = cur.next.next
        return head

    # optimal or one iteration
    def removeNthFromEnd2(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        cur = head
        first = head
        for i in range(n):
            first = first.next
        if first is None:
            head = head.next
            return head
        while first and first.next:
            cur = cur.next
            first = first.next
        cur.next = cur.next.next
        return head
