# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    # this is just changint the value
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        l = []
        while temp is not None:
            l.append(temp.val)
            temp = temp.next

        temp = head
        while temp is not None:
            temp.val = l.pop()
            temp = temp.next

    # optimal
    def optimal(self, head):
        prev = None
        temp = head
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
