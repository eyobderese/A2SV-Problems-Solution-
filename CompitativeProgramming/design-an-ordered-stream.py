class OrderedStream:

    def __init__(self, n: int):
        self.n=n
        self.list=[]
        self.tracker={}
        self.k=1
        


        

    def insert(self, idKey: int, value: str) -> List[str]:
       
        ans=[]
        if self.k==idKey:
            ans.append(value)
            self.k+=1
            while self.k in self.tracker:
                ans.append(self.tracker[self.k])
                self.k+=1
        elif self.k!=idKey:
            self.tracker[idKey]=value
        m=ans
        ans=[]
        return m

       

                


            
            


            
            


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)