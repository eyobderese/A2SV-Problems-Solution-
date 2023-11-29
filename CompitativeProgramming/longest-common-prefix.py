class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        
        i=0

        while i<len(strs[0]):
            flage = True
            value=strs[0][:len(strs[0])-i]
            for elemnts in strs:
                if value != elemnts[:len(value)]:
                    flage= False
            if flage:
                return value
                    
            else: 
                i+=1
        return ""