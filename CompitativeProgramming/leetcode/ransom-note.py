class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        tracker=defaultdict(int)
        for i in magazine:
            tracker[i]+=1
        
        count=Counter(list(ransomNote))
        for i in count.keys():
         
            if count[i]>tracker[i]:
                return False
        return True 
            