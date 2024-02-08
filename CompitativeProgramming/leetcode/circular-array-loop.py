class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n=len(nums)
        visited=set()

       
        for i in range(n):
            if i not in visited:
                tracker=set()

                
                while True:
                    
                    if i in tracker:
                        return True 
                    

                    tracker.add(i)
                    visited.add(i)
                    prev,i=i,(i+nums[i])%n

                    if prev==i:
                        break
                    if nums[prev]>0 != nums[i]<0:
                        break

        return False
                
                

            
                

       
    
            

         