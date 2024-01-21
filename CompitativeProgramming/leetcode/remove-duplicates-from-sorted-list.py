# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        store=set()

        while head:
            store.add(head.val)
            head=head.next
        store = sorted(list(store))
        if not store:
            return head
        head=ListNode(store[0])
        curr=head
        for i in range(1,len(store)):
            curr.next=ListNode(store[i])
            curr=curr.next
        return head

            

       

       
        