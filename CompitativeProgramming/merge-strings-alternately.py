class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=""
        i=0
        while i< (min(len(word1),len(word2))):
            a+=word1[i]
            a+=word2[i]
            i+=1
        if len(word1)>i:
            a+=word1[i:]
        else:
            a+=word2[i:]
        return a


        