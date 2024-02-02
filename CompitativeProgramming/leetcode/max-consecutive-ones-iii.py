class Solution:
    def longestOnes(self, nums, k):
        count=0

        i=0
        j=0
        ans=[]

        while j<len(nums):
            if nums[j]==0:
                count+=1
            if count>k:
                ans.append(j-i)
                while nums[i]==1:
                    i+=1
                i+=1
                count-=1
            j+=1
            # print(i,j)
        if count<=k:
            ans.append(j-i)
        
        return max(ans)
        