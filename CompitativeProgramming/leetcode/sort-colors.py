class Solution:
    def sortColors(self, nums):
        # for i in range(len(nums)):
        #     for j in range (len(nums)):
        #         if nums[i]<nums[j]:
        #             nums[j],nums[i]=nums[i],nums[j]
        low=0
        mid=0
        high=len(nums)-1

        while high>=mid:
            
            if nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            elif nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
            else:
                mid+=1

               
        



        
        return nums
       
        

        