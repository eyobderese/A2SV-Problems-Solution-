class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        tracker={0:-1}
        pre=[]
        summ=0
        ans=float("inf")

        for i in nums:
            summ+=i
            pre.append(summ)
        target= sum(nums)%p            
        if target==0:
            return 0

        
        for i in range(len(pre)):
            if (pre[i]%p-target)%p in tracker:
                if i-tracker[(pre[i]%p-target)%p]<len(pre):
                    ans=min(ans,i-tracker[(pre[i]%p-target)%p])
            tracker[pre[i]%p]=i
            
 

        return -1 if ans==float('inf') else ans





        
        
        

       
       
        


        