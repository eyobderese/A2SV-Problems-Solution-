class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        low=max(weights)
        high=sum(weights)

        while True:
            middVal=(low+high)//2
            if low==high:
                return middVal

            elif self.possible(middVal,weights,days):
                high=middVal
            elif not self.possible(middVal,weights,days):
                low=middVal+1
       

    def possible(self,capacity,weights,days):
        currWeight=weights[:]
        currCap=capacity
        for _ in range(days):
            while currWeight and currCap>=currWeight[-1]:
                currVal=currWeight.pop()
                currCap-=currVal
            currCap=capacity
        if not currWeight:
            return True
        return False

         
