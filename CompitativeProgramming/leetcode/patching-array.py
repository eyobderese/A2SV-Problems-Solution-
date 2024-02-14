class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """

        runningSum=0
        nums.append(n)
        count=0
    
        for i in nums: 

            if runningSum+1>=i:
                runningSum+=i
            else:
                while runningSum+1<i:
                    if runningSum>=n:
                        return count
                    
                    runningSum+=(runningSum+1)
                    count+=1
                runningSum+=i
        return count



        
        