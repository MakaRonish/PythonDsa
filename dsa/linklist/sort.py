# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        cur = head
        l.sort()
        print(l)
        for i in range(len(l)):
            cur.val = l[i]
            cur = cur.next
        return head
