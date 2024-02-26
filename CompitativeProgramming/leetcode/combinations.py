class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        self.helper(1,n,ans,[],k)
        return ans



    def helper(self,num,rang,ans,path,k):

        if len(path)==k:
            ans.append(path[:])
            return
        for n in range(num,rang+1):
            path.append(n)
            self.helper(n+1,rang,ans,path,k)
            path.pop()
        
        # return ans 






        