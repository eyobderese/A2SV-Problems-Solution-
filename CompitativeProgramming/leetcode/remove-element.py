class Solution:
    def removeElement(self, nums, val):
         j=0
         for i in range (len(nums)):
            if nums[i]!=val:
               nums[j],nums[i]=nums[i],nums[j]
               j+=1
         return(j)
