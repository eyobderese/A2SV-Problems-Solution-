class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        row,col = len(matrix),len(matrix[0])

        sum_matrix=[[0]*col for i in range(row)]

        for r in range(row):
            for c in range(col):
                top=sum_matrix[r-1][c] if r>0 else 0
                left=sum_matrix[r][c-1] if c>0 else 0
                top_left= sum_matrix[r-1][c-1] if min(r,c)>0 else 0
                sum_matrix[r][c]=matrix[r][c]+left+top-top_left
        count=0
      
        for r1 in range(row):
            for r2 in range(r1,row):
                tracker=defaultdict(int)
                tracker[0]=1
                for c in range(col):
                    
                        top=sum_matrix[r1-1][c] if r1>0 else 0
                        cur_sum=sum_matrix[r2][c]-top
                        if cur_sum-target in tracker:
                            count+=tracker[cur_sum-target]
                        tracker[cur_sum]+=1

                        # left=sum_matrix[r2][c1-1] if c1>0 else 0
                        # top=sum_matrix[r1-1][c2] if r1>0 else 0
                        # top_left=sum_matrix[r1-1][c1-1] if min(c1,r1)>0 else 0
                        # summ=sum_matrix[r2][c2]-left-top+top_left
                        # if summ==target:
                        #     count+=1
        return count


       


                
            
        