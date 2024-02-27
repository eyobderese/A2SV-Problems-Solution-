class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        store=[]
        n=len(candidates)
        def helper(curr,index):
            nonlocal store
            if sum(curr)==target:
                store.append(tuple(sorted(curr[:])))
            elif sum(curr)>target:
                index+=1
                return  
            if index==n:
                return     
            for i in range(index,n):
                curr.append(candidates[i])
                helper(curr,i)
                curr.pop()
        helper([],0)
        store=list(set(store))
        return store
            

                
        