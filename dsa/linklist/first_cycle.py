# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = set()
        cur = head
        while cur is not None:
            if cur in nodes:
                return cur
            nodes.add(cur)
            cur = cur.next
        return None

    # pointer
    def detectCycle2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fast = head
        slow = head
        while fast is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
