# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        outlist= ListNode()
        tail=outlist
        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                tail=list1
                list1=list1.next
            else :
                tail.next=list2
                tail=list2
                list2=list2.next
        while list1:
            tail.next=list1
            tail=list1
            list1=list1.next
        while list2:
            tail.next=list2
            tail=list2
            list2=list2.next
            
        outlist=outlist.next

        return outlist




        