class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=sum(nums[0:k])
        
        avrage=summ/k
        i=0
        j=k
        while j<len(nums):
            
            summ-=nums[i]
            summ+=nums[j]
            avrage=max(avrage,summ/k)
            i+=1
            j+=1
        return avrage

        

            
        