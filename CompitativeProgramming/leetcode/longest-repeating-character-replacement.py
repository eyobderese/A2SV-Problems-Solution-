from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        j=0
        longest=0
        for i in range (1,len (s)):
            count=Counter(s[j:i+1])
            maxx=max(count.values())
            if i-j-maxx+1<=k:
                longest=max(longest,i-j+1)
            else:
                j+=1
        return longest


        