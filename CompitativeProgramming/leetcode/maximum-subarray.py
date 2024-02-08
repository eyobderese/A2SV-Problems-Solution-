class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ=nums[0]
        # out=max(nums)

        # for i in range(1,len(nums)):
        #     if summ<nums[i]:
        #         summ=nums[i]
        #         out=max(out,summ)
        #     elif summ>nums[i]:
        #         summ+=nums[i]
        #         out=max(out,summ)
        #     elif summ==nums[i] and nums[i]>0:
        #         summ+=nums[i]
        #         out=max(out,summ)
        #     else:
        #         continue
        out=nums[0]
        pre=0
        for i in range(len(nums)):
            if pre<0:
                pre=nums[i]
                out=max(out,pre)

            else:
                pre+=nums[i]
                out=max(out,pre)
            
        return out




        