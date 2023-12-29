class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x:x[0])
        maxx=0
        for i in range(len(points)-1):
            width=points[i+1][0]-points[i][0]
            maxx=max(width,maxx)
        return maxx
        