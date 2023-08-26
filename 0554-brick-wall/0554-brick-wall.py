class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        ## create a hashmap for counting gaps at every postion 
        ## initialize it with 0,0
        
        countGap = {0:0}
        
        for r in wall:
            total = 0
            ## every brick position except the last because its mentioned in the question
            for b in r[:-1]:
                total+=b
                countGap[total] = 1 + countGap.get(total,0)
                
        return len(wall) - max(countGap.values())      
        