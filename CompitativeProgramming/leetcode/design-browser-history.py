class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.head=ListNode(homepage)
        self.current=self.head


        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        newNode=ListNode(url)
        self.current.next=newNode
        newNode.prev=self.current
        self.current=newNode
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps>0 and self.current.prev:
            self.current=self.current.prev
            steps-=1
        return self.current.val
        


        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps>0 and self.current.next:
            self.current=self.current.next
            steps-=1
            
        return self.current.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None