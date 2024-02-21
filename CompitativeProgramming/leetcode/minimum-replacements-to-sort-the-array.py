class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count=0

        checker=nums[-1]        
        j=len(nums)-1
        while j>=0:      
            if nums[j]>checker:
                
                space=nums[j]//checker
                if nums[j]%checker!=0:
                    space+=1
                count+=(space-1)

                checker=nums[j]//space

            elif nums[j]<=checker:
                checker=nums[j]

            j-=1

        return count
        