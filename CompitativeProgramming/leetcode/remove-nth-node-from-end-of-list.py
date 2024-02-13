# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = cur_node = ListNode()
        dummy.next=head

        curr =dummy
        count=-1
      

        while cur_node: 
            cur_node = cur_node.next 
            count+=1
        
        k=count-n
        print(k)
        if k<0:
            return head
        
        curr=dummy
        for i in range(k):
            curr=curr.next
        print(curr.val)
        if curr and curr.next:
            curr.next=curr.next.next
        else:
            curr.next=None
        
        return dummy.next
        
        
        


        


       




        