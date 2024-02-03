class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        leftPrf=[]
        rightPrf=[]
        leftsum=0
        rightsum=0
        j=len(nums)-1
        for i in nums:
            leftsum+=i
            leftPrf.append(leftsum)
            rightsum+=nums[j]
            rightPrf.append(rightsum)
            j-=1
        rightPrf=rightPrf[::-1]
        print(rightPrf,leftPrf)
        for i in range(len(rightPrf)):
            if rightPrf[i]==leftPrf[i]:
                return i
        return -1 
        