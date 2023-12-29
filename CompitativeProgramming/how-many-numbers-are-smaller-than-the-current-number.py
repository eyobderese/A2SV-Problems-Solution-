class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        myCounter=[]
        # for i in range(len(nums)):
        #     count=0
        #     for j in nums:
        #         if j<nums[i]:
        #             count+=1
        #     myCounter.append(count)
        # return myCounter
        
        tempList=sorted(nums)
        for i in range (len(nums)):
          
            indexx = tempList.index(nums[i])
            myCounter.append(indexx)
        return myCounter