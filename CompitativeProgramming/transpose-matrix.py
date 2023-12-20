class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])

        j=0
        ans=[]
        while j<m:
            row=[]
            i=0
            
            while i<n:
                row.append(matrix[i][j])
                i+=1
            ans.append(row)
            j+=1
        return ans


        