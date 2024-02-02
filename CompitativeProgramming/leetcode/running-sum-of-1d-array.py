class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total =0
        res=[]

        for i in nums:
            total+=i
            res.append(total)
        return res