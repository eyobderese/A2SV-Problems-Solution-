# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        size=0
        curr=head
        index=0
        while curr:
            size+=1
            curr=curr.next
        if size%2==0:
            index=(size/2)+1
        else:
            index=(size+1)/2
        curr=head
        for i in range(int(index)-1):
            curr=curr.next
        
        return curr

        
        