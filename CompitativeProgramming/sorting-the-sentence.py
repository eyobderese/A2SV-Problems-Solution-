class Solution:
    def sortSentence(self, s: str) -> str:
        ans=s.split()
        ans.sort(key=lambda x:x[-1])
        m=''
        for i in ans:
            m+=i[:len(i)-1]
            m+=" "
        return m.strip()
        
