class Solution:
    def printVertically(self, s: str) -> List[str]:
        list_of_word=s.split()
        ans=[]
        flag=True
        j=0
        while flag:
            flag=False
            m=""
            for i in list_of_word:
                if j<len(i):
                    flag=True
                    m+=i[j]
                else:
                    m+=" "
            j+=1
            m=m.rstrip()
            if m:      
                ans.append(m)
        return ans
        

                

        