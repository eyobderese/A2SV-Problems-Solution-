class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        column=[]
        n=len(grid)
        for i in range(n):
            ans=float("-inf")
            for j in range(n):
                ans=max(grid[j][i],ans)
            column.append(ans)
        row=[]
        for ro in grid:
            row.append(max(ro))
        ans=0
        for i in range(n):
            for j in range(n):
                ans+=min(row[i],column[j])-grid[i][j]
        return ans

                

