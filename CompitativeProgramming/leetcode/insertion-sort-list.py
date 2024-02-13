# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumyNode=ListNode(0,head)
        cur=head.next
        prv=head

        while cur:
            if cur.val>=prv.val:
                prv=cur
                cur=cur.next
                continue
            tracker=dumyNode
            while tracker.next.val<cur.val:
                tracker=tracker.next
            prv.next=cur.next    
            cur.next=tracker.next
            tracker.next=cur
            cur=prv.next
        return dumyNode.next

        

        
            
            
        

                    
        