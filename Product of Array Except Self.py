class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # out=[]
        # total=1
        # pre=1
        
        # for i in range(len(nums)):
            
        #     j=i+1
        #     if i >0:
        #         pre*=nums[i-1]

        #     while j<len(nums):
        #         total*=nums[j]
        #         j+=1                          brutForse Solution
            
        #     out.append(total*pre)
        #     total=1
        # return out

        pre=[1]
        suf=[1]
        total=1
        total2=1
        out=[]

        for i in range(0,len(nums)-1):
            total*=nums[i]
            pre.append(total)

            total2*=nums[len(nums)-i-1]
            suf=[total2]+suf
        for i in range(len(nums)):
            out.append(pre[i]*suf[i])
        return out
        
        
        





       

            