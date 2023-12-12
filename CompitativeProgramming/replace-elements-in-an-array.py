class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        A={}
        j=0
        for i in nums:
            A[i]=j
            j+=1
        
        for i,k in operations:

            index=A[i]
            nums[index]=k
            del A[i]
            A[k]=index
        return nums
        