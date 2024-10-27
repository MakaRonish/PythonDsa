# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        odd=head
        even=head.next
        l=[]
        l.append(odd.val)
        while odd.next and odd.next.next:
            odd=odd.next.next
            l.append(odd.val)
        print(l)
        l.append(even.val)
        while even.next and even.next.next:
            even=even.next.next
            l.append(even.val)
        print(l)
        cur=head
        for i in range(len(l)):
            cur.val=l[i]
            cur=cur.next
        return head
    # optimal
    def opt(self,head):
        
