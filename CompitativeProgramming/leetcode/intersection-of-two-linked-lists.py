# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tracker=set()

        curr=headA

        while curr:
            tracker.add(curr)
            curr=curr.next
        
        curr=headB
        while curr:
            if curr in tracker:
                return curr
            curr=curr.next
        
        return 
        
        