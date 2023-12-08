class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        tracker= defaultdict(int)
        winner=[]

        for i,j in matches:
            tracker[j]+=1
            winner.append(i)
        
        winer=[]
        losser=[]

        for i in tracker.keys():
            if tracker[i]==1:
                losser.append(i)
        for i in winner:
            if i not in tracker.keys() and i not in winer:
                winer.append(i)
        return [sorted(winer),sorted(losser)]
            

        

        