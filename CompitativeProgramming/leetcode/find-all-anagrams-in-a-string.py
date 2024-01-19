class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        answer=[]
        p=''.join(sorted(p))

        i=0
        j=len(p)

        while j<=len(s):
            m=''.join(sorted(s[i:j]))
            if p==m:
                answer.append(i)
            
            i+=1
            j+=1

        return answer