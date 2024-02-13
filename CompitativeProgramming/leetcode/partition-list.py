# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not (head and head.next):
            return head

        dummyLess = lessNode=ListNode()
        dummyGreat = greaterNode=ListNode()

        while head:
            if head.val<x:
                lessNode.next = head 
                lessNode = lessNode.next
            else:
                greaterNode.next = head 
                greaterNode = greaterNode.next 
            head = head.next 

        lessNode.next = dummyGreat.next 
        greaterNode.next = None 

        return dummyLess.next 




        