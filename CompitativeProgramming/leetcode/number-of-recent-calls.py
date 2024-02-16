class RecentCounter(object):

    def __init__(self):
        self.queu=deque()
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queu.append(t)
        while self.queu and self.queu[0]<t-3000:
            self.queu.popleft()
        return len(self.queu)
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)