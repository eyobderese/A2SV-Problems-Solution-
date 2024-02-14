# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        n=0

        curr=head

        while curr:
            n+=1
            curr=curr.next
        eachLength=n//k
        leftRem=n%k

        ans=[None]*k
        curr=head
        pointer=0
    
        if k>=n:
            while curr:
                ans[pointer]=(curr)
                pointer+=1
                prev=curr
                curr=curr.next
                prev.next=None
            return ans
        

        curr=head
        prev=head
        count=0
        rem=1
        
        while curr:
            prev=curr
            curr=curr.next
            count+=1

            if not leftRem:
                rem=0
            if count==eachLength+rem:
                prev.next=None
                ans[pointer]=head
                pointer+=1
                head=curr
                count=0
                leftRem-=1
                
      

    
        return ans
        

        
        

        


            

        