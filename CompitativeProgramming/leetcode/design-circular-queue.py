class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k
        self.size=0
        self.head=Node(0)
        self.tail=Node(0)
        self.head.next=self.tail
        self.tail.prev=self.head


        

    def enQueue(self, value: int) -> bool:
        if self.size!=self.k:
            end=self.tail.prev
            newNode=Node(value)
            end.next=newNode
            newNode.prev=end
            newNode.next=self.tail
            self.tail.prev=newNode
            self.size+=1
            return True
        return False
        

    def deQueue(self) -> bool:
        if self.size!=0:
            first=self.head.next
            ans=first.val
            self.head.next=first.next
            first.next.prev=self.head
            self.size-=1
            return True
        return False
        

    def Front(self) -> int:
        if self.size!=0:
            print(self.head.next,self.size)
            return self.head.next.val

        return -1
        
    def Rear(self) -> int:
        if self.size!=0:
            return self.tail.prev.val
        return -1
        

    def isEmpty(self) -> bool:
        if self.size==0:
            return True
        return False
         
    def isFull(self) -> bool:
        if self.size==self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
        self.prev=None