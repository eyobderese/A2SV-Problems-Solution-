class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if nums==sorted(nums):return True
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                temp=nums[i]
                nums[i]=nums[i+1]

                if not nums==sorted(nums):
                    nums[i]=temp
                    nums[i+1]=temp
                    if nums==sorted(nums):
                        return True
                    else:
                        return False
                return True

               



             

        