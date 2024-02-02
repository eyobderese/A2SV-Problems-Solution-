class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=0
        j=0
        count=0
        n_nice=0
        sub=0
        while j<len(nums):
            if nums[j]%2!=0:
                count+=1
                sub=0

                
            while count>=k:
                if nums[i]%2!=0:
                    count-=1
                sub+=1
                i+=1
            j+=1
            n_nice+=sub
        return n_nice
            
