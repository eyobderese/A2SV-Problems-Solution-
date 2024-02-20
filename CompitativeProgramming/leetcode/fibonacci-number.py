class Solution:
        
    Adict={}
    def fib(self, n: int,Adict=Adict) -> int:
        if n in Adict:
            return Adict[n]
        if n==2 or n==1:
            return 1
        if n==3:
            return 2
        if n==0:
            return 0
        Adict[n]=self.fib(n-1,Adict)+self.fib(n-2,Adict)
        return self.fib(n-1,Adict)+self.fib(n-2,Adict)
        