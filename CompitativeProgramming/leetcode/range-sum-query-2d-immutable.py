class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix=[[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.prefix[i+1][j+1]=matrix[i][j]-self.prefix[i][j]+self.prefix[i][j+1]+self.prefix[i+1][j]
              

        



        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefixSum=self.prefix
       
        return prefixSum[row2+1][col2+1]-prefixSum[row1][col2+1]-prefixSum[row2+1][col1]+ prefixSum[row1][col1]


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)