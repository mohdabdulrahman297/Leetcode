class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ## create two hashsets/dictionary for finding duplicates , both for rows and columns
        
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        
        ## also create a hashset for each 3*3 grid
        
        squares = collections.defaultdict(set) # key = (r/3 , c/3)
        
        for r in range(9):
            for c in range(9):
                ## if the value is "." move to the next iteration
                if(board[r][c] == "."):
                    continue
                  
                if(board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3 , c//3)]):
                    return False
                ## and if no duplicates then add values into the board
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3 , c//3)].add(board[r][c])
              
                        
                        
        return True             
        