class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        pref=[]

        summ=0
        for i in nums:
            summ+=i
            pref.append(summ)
        tracker=defaultdict(int)
        tracker[0]=1
        count=0
        for i in pref:
            count+=tracker[i-goal]
            tracker[i]+=1
        return count
            
    
      