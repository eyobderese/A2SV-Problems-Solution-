class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n=len(matrix)
        m=n-1
        for i in range(n):
            for j in range(i,n):
                print(matrix[i][j],matrix[j][i])

                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        print(matrix)
        for i in range(n):
            matrix[i]=matrix[i][::-1]
        
            

                
        