class Solution:
    def longestSubarray(self, nums):

        count=0

        i=0
        j=0
        ans=[]

        while j<len(nums):
            if nums[j]==0:
                count+=1
            if count>1:
                ans.append(j-i)
                while nums[i]==1:
                    i+=1
                i+=1
                count-=1
            j+=1
            # print(i,j)
        if count<=1:
            ans.append(j-i)
        
        return max(ans)-1
            
        