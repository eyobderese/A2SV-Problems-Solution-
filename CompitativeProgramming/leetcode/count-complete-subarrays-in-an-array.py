class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=len(set(nums))
        count=0
        j=0

        for i in range(len(nums)):
            while len(set(nums[j:i+1]))==k:
                count+=(len(nums)-i)
                j+=1
            
        return count
