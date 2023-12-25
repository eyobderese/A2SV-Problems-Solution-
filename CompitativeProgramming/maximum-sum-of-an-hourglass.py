class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        col=len(grid[0])
        row=len(grid)
        i=0
        j=1
        k=2

        summ=0
        while k<row:
            l=0
            m=1
            n=2
            while n<col:
                add=grid[i][l]+grid[i][m]+grid[i][n]+grid[j][m]+grid[k][l]+grid[k][m]+grid[k][n]
                summ=max(add,summ)
                l+=1
                m+=1
                n+=1
            i+=1
            j+=1
            k+=1
        return summ


        


        