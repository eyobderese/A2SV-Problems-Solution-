class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        tracker=defaultdict(int)
        counter=0
        n=len(nums)
        k=1
        for i in nums:
            counter+=i
            tracker[k]=counter
            k+=1
        ans=defaultdict(list)
        maxx=0
        for i in range(n+1):
            n_0=i-tracker[i]
            n_1=tracker[n]-tracker[i]
            ans[n_0+n_1].append(i)
        m=max(ans.keys())
        return ans[m]

            
        


        