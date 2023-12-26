class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
      
        count=0
        maxx=1
        count1=0
        for i in range(len(flips)):
            maxx=max(maxx,flips[i])
            count1+=1


            
            if maxx==count1:
                count+=1
            
        return count
     

      
        return count


        