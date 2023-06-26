class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ##create an answer 
        result = [[1]]
        
        ##iterate through number of rows i.e numsRows
        for i in  range(numRows - 1):
            ##add a zero in the beginning and end of the row and store it into a temp 
            temp = [0] + result[-1] + [0]
            ## create an empty row
            row = []
            ## building the next row = length of previous row + 1
            for j in range(len(result[-1]) + 1 ):
                ## temp[j] and tep[j+1] are two pointers 
                row.append(temp[j] + temp[j+1]) 
            result.append(row)
            
        return result   
        