class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        
        while start<=end:
            midd=(start+end)//2
            if nums[midd]>target:
                end=midd-1
            elif nums[midd]<target:
                start=midd+1
            else:
                return midd
        return -1
                    
        