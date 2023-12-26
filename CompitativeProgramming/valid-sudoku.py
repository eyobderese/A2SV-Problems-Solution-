

               

def triple (board,m,k):
    tracker=set()
    n=m
    while n<m+3:
        j=k
        while j<k+3:
            if board[n][j]!="." and board[n][j] in tracker:
                return False
            else:
                print(n,j,board[n][j])
                tracker.add(board[n][j])
                j+=1


        n+=1
    return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        i=0
        
        while i<9:
            j=0
            tracker2=set()
            while j<9:
                if board[i][j]!="." and board[i][j] in tracker2:
                    return False
                else:
                    tracker2.add(board[i][j])
                    j+=1
            i+=1
        k=0
        
        while k<9:
            j=0
            tracker2=set()
            while j<9:
                if board[j][k]!="." and board[j][k] in tracker2:
                    
                    return False
                else:
                    tracker2.add(board[j][k])
                    j+=1
            k+=1
        
        j=0
        while j<9:
            k=0
            while k<9:
                m=triple(board,j,k)
                if m:
                    k+=3
                else:
                    return False
            j+=3
        return True
        


            

                


                
        
       
            










            



    


        