class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=10**9 + 7
        n_even=n//2
        n_odd=n//2
        n_even+=n%2

        

        return (self.myPow(5,n_even,MOD) * self.myPow(4,n_odd,MOD))%MOD
    
    
    def myPow(self, x: float, n: int,mod:int) -> float:

        if n==-1:
            return 1/x 
        elif n<0:
            rem=n%2
            return ((self.myPow(x,n//2,mod))**2 *self.myPow(x,rem,mod))%mod
        elif n==0:
            return 1
        elif n==1:
            return x
        else:
            rem=n%2
            return ((self.myPow(x,n//2,mod))**2 *self.myPow(x,rem,mod))%mod

            



        
     