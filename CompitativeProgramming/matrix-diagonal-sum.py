class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0

        i=0
        while i<len(mat):
            j=0
            while j<len(mat[0]):
                if i-j==0 or i+j==len(mat)-1:
                    summ+=mat[i][j]
                j+=1
            i+=1
        return summ


        