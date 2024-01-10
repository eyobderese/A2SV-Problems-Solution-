class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=['a','e','i','o','u']
        count=0
        j=0
        n_vaowl=0
        subString= s[0:k]
        for i in subString:
            if i in vowel:
                n_vaowl+=1
        count=max(count,n_vaowl)

        for i in range(k,len(s)):
            if s[i] in vowel:
                n_vaowl+=1
            if s[j] in vowel:
                n_vaowl-=1
            j+=1
            count=max(count,n_vaowl)
        return count

            