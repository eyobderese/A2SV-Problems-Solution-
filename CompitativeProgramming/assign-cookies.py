class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        j=0
        counter=0
        while i<len(g) and j<len(s):
            while g[i]>s[j]:
                j+=1
                if j>=len(s):
                    return counter
            counter+=1
            j+=1
            i+=1
        return counter
            
        