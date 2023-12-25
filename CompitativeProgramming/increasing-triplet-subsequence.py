class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small=nums[0]
        small2=float(inf)
        for i in nums:
            if i<small:
                small=i
            elif i>small and i<small2:
                small2=i
            elif i>small2:
                return True
        return False

        
        

            



        