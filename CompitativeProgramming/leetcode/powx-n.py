class Solution:
  
    def myPow(self, x: float, n: int) -> float:
        
     
        if n==-1:
            return 1/x 
        elif n<0:
            rem=n%2
            return (self.myPow(x,n//2))**2 *self.myPow(x,rem)
        elif n==0:
            return 1
        elif n==1:
            return x
        else:
            rem=n%2
            return (self.myPow(x,n//2))**2 *self.myPow(x,rem)
        