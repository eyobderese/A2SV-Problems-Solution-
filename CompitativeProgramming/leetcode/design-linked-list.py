class MyLinkedList(object):

    def __init__(self):
        self.size=0
        self.head=Node(0)

      



        

        

        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """

        
        curr=self.head
        if index>=self.size:
            return -1
        
        for i in range(index):
            # print(curr.val)
            curr=curr.next
            
        return curr.val

                



        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: 
        """
        if self.size==0:
            self.head=Node(val)
        else:
            temp=self.head
            self.head=Node(val)
            self.head.next=temp
        self.size+=1

        # self.traverse()
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: 
        """
        if self.size==0:
            self.head=Node(val)
            self.size+=1
        else:
            curr=self.head
            for i in range(self.size-1):
                curr=curr.next
            curr.next=Node(val)
            self.size+=1
            # self.traverse()


        


        
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: 
        """

        
        curr=self.head.next
        prev=self.head

        if index==0:
            self.addAtHead(val)
        elif index>self.size:
            return
        else:
            for _ in range(index-1):
                curr=curr.next
                prev=prev.next

            newNode=Node(val) 
            temp=curr
            prev.next=newNode
            newNode.next=temp
            self.size+=1

        




        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: 
        """
        self.traverse()

        if index>=self.size:
            return 
        if index==0:
            self.head=self.head.next

        else:
            prev=self.head
            curr=self.head.next
            index-=1
            
            while index>0 and curr:
                prev=prev.next
                curr=curr.next
                index-=1
                
            prev.next=curr.next
        self.size-=1

    def traverse(self):
        curr=self.head
        for i in range(self.size):
            print(curr.val)
            curr=curr.next
  



     
     


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
