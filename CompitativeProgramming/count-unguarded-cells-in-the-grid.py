class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        
        matrix= [['M' for i in range(n)] for i in range (m)]

        for i,j in walls:
            matrix[i][j]='w'
        for i,j in guards:
            matrix[i][j]='g'

        for i,j in guards:
            k=j+1
            while k<n:
                if matrix[i][k]!='w' and matrix[i][k]!="px":
                    matrix[i][k]='px'
                    k+=1
                else:
                    break
            k=j-1
            while k>=0:
                if matrix[i][k]!='w' and matrix[i][k]!="px":
                    matrix[i][k]='px'
                    k-=1
                else:
                    break
        for i,j in guards:
            k=i-1
            while k>=0:
                if matrix[k][j]!='w' and matrix[k][j]!="py":
                    matrix[k][j]='py'
                    k-=1
                else:
                    break
            k=i+1
            while k<m:
                if matrix[k][j]!='w' and matrix[k][j]!="py":
                    matrix[k][j]='py'
                    k+=1
                else:
                    break
            
            

        



       



        
        count=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='M':
                    count+=1
        return count
