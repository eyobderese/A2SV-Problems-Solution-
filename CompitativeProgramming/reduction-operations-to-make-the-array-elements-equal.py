class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        setnums=set(nums)
        listnums=sorted(list(setnums))

        tracker={}
        k=0
        for i in listnums:
            tracker[i]=k
            k+=1
        count=0
        for i in nums:
            count+=tracker[i]
        return count

       
            
        
        