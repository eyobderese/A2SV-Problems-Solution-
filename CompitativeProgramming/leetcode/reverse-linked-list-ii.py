# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left==right or not head or not head.next:
            return head
        dummyNode=ListNode()
        dummyNode.next=head

        curr=dummyNode
        for _ in range(left-1):
            curr=curr.next
        nonReverseStart=curr
        reverseStart=curr.next
        for _ in range(right-left+1):
            curr=curr.next
        reverseend=curr
    
        nonRevereEnd = reverseend.next
        reverseend.next=None
        reversedHead,reversedEnd=self.reverseList(reverseStart)

        nonReverseStart.next=reversedHead
        reversedEnd.next=nonRevereEnd

        return dummyNode.next
        
    

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        
    
        prev=None
        curr=head
        end=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        return prev,end


        

        
        return dummyNode.next


        