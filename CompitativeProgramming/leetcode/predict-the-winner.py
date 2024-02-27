class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        i=0
        j=len(nums)-1
        turn=True
        summ=0
        def helper(i,j,turn):
            if i>j:
                return 0 
            elif turn:
                return max(nums[i]+helper(i+1,j,(not turn)),nums[j]+helper(i,j-1,(not turn)))
            
            else:
                return min(-nums[i]+helper(i+1,j,(not turn)),-nums[j]+helper(i,j-1,(not turn)))

        
    
        if helper(i,j,True)>=0:
            return True
        return False 
            

        