class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        
        i=0
        j=n-1
        counter=0

        while j>i:
            summ=nums[i]+nums[j]
            if summ==k:
                

                counter+=1
                i+=1
                j-=1
            elif summ>k:
                j-=1
            else:
                i+=1
        return counter
            



        