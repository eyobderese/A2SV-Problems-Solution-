class MyStack:

    def __init__(self):
        self.first=Queue()
        self.second=Queue()
        self.size=0
        
        

    def push(self, x: int) -> None:
        self.first.push(x)
        self.size+=1
        

    def pop(self) -> int:
        size=self.size
        while self.size!=0:
            m=self.first.pop()
            self.second.push(m)
            self.size-=1
        ans=self.second.popR()
        while self.size!=size-1:
            n=self.second.pop()
            self.first.push(n)
            self.size+=1
        return ans
        

    def top(self) -> int:
        m=self.first.top()
        return m 

        

    def empty(self) -> bool:
        if self.size==0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

class Queue:
    def __init__(self):
        self.queue=deque()
        self.size=0
    
    def push(self,x):
        self.queue.append(x)
        self.size+=1
    def pop(self):
        if self.size!=0:
            m=self.queue.popleft()
            self.size-=1
            return m
        return -1
    def popR(self):
        return self.queue.pop()

    def top(self):
        if self.size!=0:
            return self.queue[-1]
        return -1
            

    