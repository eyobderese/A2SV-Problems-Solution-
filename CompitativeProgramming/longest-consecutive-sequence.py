class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        counter=1
        maxx=0

        if len(nums)<1:
            return 0

        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]-1 :
                counter+=1
            elif nums[i]<nums[i+1]-1:
                print(maxx,counter)
                maxx=max(counter,maxx)
                counter=1
        maxx=max(counter,maxx)
        
        return maxx


       
        
     

        