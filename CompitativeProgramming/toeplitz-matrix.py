class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n=len(matrix)
        m=len(matrix[0])
        for i in range (n-1):
            for j in range(m-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True

            



        