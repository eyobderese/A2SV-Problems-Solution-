class Solution:
    def lengthOfLongestSubstring(self, s):
        longest,i,j=0,0,0
        while j<len(s):
            if s[j] not in s[i:j]:
                j+=1
                
            else:
                longest=max(longest,j-i)
                i+=1
                
        longest = max(longest, j-i)
        return longest
        