class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessthan=[]
        graterthan=[]
        equal=[]
        for i in nums:
            if i>pivot:
                graterthan.append(i)
            elif i<pivot:
                lessthan.append(i)
            else:
                equal.append(i)
        return lessthan + equal+ graterthan 

                
        