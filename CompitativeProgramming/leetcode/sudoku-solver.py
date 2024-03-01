class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def findCell(row,col):
            if col<3:
                if row<3:
                    return 1
                if row<6:
                    return 2
                return 3
            if col<6:
                if row<3:
                    return 4
                if row<6:
                    return 5
                return 6
            else:
                if row<3:
                    return 7
                if row<6:
                    return 8
                return 9

        rowTracker=defaultdict(set)
        columnTracker=defaultdict(set)
        cellTracker=defaultdict(set)

        
            

        for row in range(9):
            for col in range(9):
                if board[row][col]==".":
                    continue
                rowTracker[row].add(int(board[row][col]))
                columnTracker[col].add(int(board[row][col]))
                cellTracker[findCell(row,col)].add(int(board[row][col]))
        
        def helper(row,col):
            if row==9:
                return True
            if col==9:
                return helper(row+1,0)
                 
            if board[row][col]!=".":
                return  helper(row,col+1)
                

            
            
            for numb in range(1,10):
                if numb in rowTracker[row] or numb in columnTracker[col] or numb in cellTracker[findCell(row,col)]  :
                    continue

                board[row][col]=str(numb)
                rowTracker[row].add(numb)
                columnTracker[col].add(numb)
                cellTracker[findCell(row,col)].add(numb)
                if helper(row, col+1)==True:
                    return True
                rowTracker[row].remove(numb)
                columnTracker[col].remove(numb)
                cellTracker[findCell(row,col)].remove(numb)
                board[row][col]="."

        helper(0,0)


            


        





        




                    
                
            


        