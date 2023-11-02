class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:


        # ans=''
        # dictTrack={i:0 for i in range(len(s))}    Brut force solution
        

        # for st,end,dirr in shifts:
        #     if dirr==0:
        #         while end>=st:
        #             dictTrack[end]-=1
        #             end-=1
        #     else:
        #         while end>=st:
        #             dictTrack[end]+=1
        #             end-=1
        # for i in range(len(s)):
        #     newCal= ((ord(s[i])-97 +dictTrack[i]))%26 +97


        #     ans+=chr(newCal)
            
        # return ans
        ans=''
        tracker=[0 for i in range (len(s)+1)]

        for st,end,dirc in shifts:
            if dirc==0:
                tracker[st]-=1
                tracker[end+1]+=1

            else:
                tracker[st]+=1
                tracker[end+1]-=1
        total=0
        preFixSum=[]
        for i in tracker:
            total+=i
            preFixSum.append(total)
        
        for i in range(len(s)):
            newCal= ((ord(s[i])-97 + preFixSum[i]))%26 +97
           

            ans+=chr(newCal)
            
        return ans
        