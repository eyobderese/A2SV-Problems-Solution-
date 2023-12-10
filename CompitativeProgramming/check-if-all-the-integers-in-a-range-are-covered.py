class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges=sorted(ranges)
        tracker={}
        tracker[ranges[0][0]]=ranges[0][1]
        for i,j in ranges:
            keys=list(tracker.keys())
            
            if i <= tracker[keys[-1]]+1 and j>tracker[keys[-1]] :
                tracker[keys[-1]]=j
            elif i <= tracker[keys[-1]] and j<=tracker[keys[-1]]:
                continue
            else:
                tracker[i]=j
        print(tracker)
        for i in tracker:
            if i<= left and tracker[i]>=right:
                return True
        return False
           



        
        
        