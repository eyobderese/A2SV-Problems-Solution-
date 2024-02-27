class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        n=len(weights)
        store=[0]*(n-1)

        for i in range(n-1):
            store[i]=weights[i]+weights[i+1]
        
        store.sort()
        ans=0
        for i in range(k-1):
            ans+=(store[n-2-i]-store[i])
        return ans



        