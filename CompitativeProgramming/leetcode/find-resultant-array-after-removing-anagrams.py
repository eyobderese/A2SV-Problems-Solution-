class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans=[]
        ans.append(words[0])
        for i in range(len(words)-1):
            if sorted(words[i])==sorted(words[i+1]):
                continue
            ans.append(words[i+1])
        return ans


       
            



        