# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        z = l[::-1]
        return z == l

    # less space more time
    def isPalindrome2(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next

        cur = head

        while cur:
            a = l.pop()
            if a != cur.val:
                return False
            cur = cur.next
        return True

    def pointers(self, head):
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            fast = fast.next.next
        next_link = slow
        prev = None
        while next_link:
            next = next_link.next
            next_link.next = prev
            prev = next_link
            next_link = next
        cur = head
        while prev:
            if prev.val != cur.val:
                return False
            cur = cur.next
            prev = prev.next
