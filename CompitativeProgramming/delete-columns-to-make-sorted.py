class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m=len(strs)
        n=len(strs[0])

        i=0
        count=0
        while i<n:
            j=0
            a=''
            while j<m:
                a+=strs[j][i]
                j+=1
            if a!=''.join(sorted(a)):
                count+=1
            i+=1
        return count





        