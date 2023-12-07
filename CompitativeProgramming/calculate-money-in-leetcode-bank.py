class Solution:
    def totalMoney(self, n: int) -> int:
      ans=0
      counter=0
      rate=1
      for i in range(0,n):
        ans+=i%7+rate
        counter+=1
        print('counter ',counter, '  ans: ',ans)
        if counter==7:
          rate+=1
          counter=0
      return ans
      
      
     

      

   
      
     

      


