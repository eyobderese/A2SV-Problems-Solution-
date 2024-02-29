class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans=set()
        temp=[]
        tracker=set()
        n=len(candidates)
        candidates.sort()
        def helper(index,temp):
            nonlocal ans
            summ=sum(temp)

            if summ==target:
                ans.add(tuple(sorted(temp)))
                return
            if summ>target or index>=n:
                return
            
            for i in range(index,n):
                if i>index and candidates[i]==candidates[i-1]:
                    continue 
                temp.append(candidates[i])
                helper(i+1,temp)
                temp.pop()
        helper(0,[])
        return  list(ans)

        