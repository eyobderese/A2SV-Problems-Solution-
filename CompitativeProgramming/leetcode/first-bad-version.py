# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        start=1
        end=n
        while True:
            midd=(start+end)//2
            if start==end:
                return start  
            elif isBadVersion(midd):
                end=midd                      
            elif not isBadVersion(midd):
                start=midd+1
                


        