class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        index=0
        n=len(word)
        maxRow=len(board)
        maxCol=len(board[0])
        visited=[]
        def helper(row,col,index):
            nonlocal visited
            if index==n:
                return True
            if row==maxRow or row==-1:
                return
            if col==maxCol or col ==-1:
                return 
            if board[row][col]!=word[index]:
                return
            if (row,col) in visited:
                return
            if board[row][col]==word[index]:
                index+=1
            visited.append((row,col))


            v1=helper(row+1,col,index)
                     
            v2=helper(row-1,col,index)
           
           
            v3=helper(row,col+1,index)

            v4=helper(row,col-1,index)

            visited.pop()

            return v1 or v2 or v3 or v4
        for row in range(maxRow):
            for col in range(maxCol):
                ans=helper(row,col,0)
                if ans:
                    return True
        return False



        





        