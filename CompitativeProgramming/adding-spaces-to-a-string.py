class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m=0
        for i in spaces:

            s=s[0:i+m]+" "+s[i+m:]
            m+=1
        return s