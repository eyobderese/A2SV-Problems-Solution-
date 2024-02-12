# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not(head and head.next and head.next.next):
            return head
        

        curr=head
        evenhead=head.next
        evencurrent=head.next

        while curr and curr.next and curr.next.next:
            curr.next=evencurrent.next
            evencurrent.next=curr.next.next
            curr=curr.next
            evencurrent=evencurrent.next
        curr.next=evenhead

        return head

        