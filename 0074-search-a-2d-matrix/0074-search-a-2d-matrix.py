## space: o(1)
## time: o(logm + logn)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ## initialize the rows and columns
        
        ROWS, COLS = len(matrix), len(matrix[0])  # ROWS = 3, COLS = 4
        top, bot = 0, ROWS - 1  # Initialize pointers for the first         binary search
        
        ##iterate and the find the rows where the target is expected
        
        while(top <= bot):
            ## calculate the row 
            row = (top + bot) // 2
            
            ## now compare the target with max value of the row
            
            if(target > matrix[row][-1]):
                top = row+1
            ## now compare the target with least value of the row    
            elif(target < matrix[row][0]):
                bot = row-1
                
            else:
                 break
                    
        if not(top <= bot):
            return False
        
        ## now perform binary search in the row we got from the previous operation
        
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while(l <= r):
            m = (l+r) // 2
            if(target > matrix[row][m]):
                l = m+1
            elif(target < matrix[row][m]):
                r = m-1
            else:
                return True
        return False    
        
                                
        
        
        