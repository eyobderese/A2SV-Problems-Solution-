class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums=sorted(nums,reverse=True)
        for i in range(len(nums)-2):
            parametr=nums[i]+nums[i+1]+nums[i+2]
            s=parametr/2
            print(parametr,s)
            if nums[i]<nums[i+1]+nums[i+2] and  nums[i]+nums[i+1]>nums[i] and nums[i] + nums[i+2]>nums[i+1]:
                return parametr
        return 0



        