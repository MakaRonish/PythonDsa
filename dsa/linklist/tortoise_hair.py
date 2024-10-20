# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def middleNode(self, head):
        tor = head
        fast_tor = head
        # while fast_tor is not None and fast_tor.next is not None :
        while fast_tor and fast_tor.next:
            tor = tor.next
            fast_tor = fast_tor.next.next
        return tor
