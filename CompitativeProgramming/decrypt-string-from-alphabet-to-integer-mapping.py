class Solution:
    def freqAlphabets(self, s: str) -> str:

        Tdict={}
        ans=[]
        start=1
        
        for i in range (97,123):
            Tdict[start]=chr(i)
            start+=1
        Nohash=s.count("#")
        count_hash=0
        s=(s.strip().split("#"))
        print(s)
        for i in s:
            if len(i)==0:
                continue
            elif count_hash==Nohash:
                for j in i:
                    ans.append(Tdict[int(j)])
            elif len(i)>2:
                count_hash+=1
                for j in range(len(i)-2):
                    ans.append(Tdict[int(i[j])])
                ans.append(Tdict[int(i[len(i)-2:])])

            else:
                ans.append(Tdict[int(i)])
                count_hash+=1

        return ''.join(ans)




        


        
        
        
 




        