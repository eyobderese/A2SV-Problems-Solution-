class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarterTimes=len(arr)/4

        dictCounter=Counter(arr)
        for i in dictCounter:
            if dictCounter[i]>quarterTimes:
                return i
        
        