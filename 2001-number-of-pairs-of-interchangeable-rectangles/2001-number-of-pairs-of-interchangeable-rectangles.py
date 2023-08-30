##Time complexity : O(n)
##Space complexity: O(n)
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        ## create a hashmap as follows
        
        count = {} # {w/h : count}
        
        res = 0
        
        for w , h in rectangles:
            
            #increament the count for ratio
            
            count[w/h] = count.get(w/h , 0) + 1
            
            #  we calculate the number of pairs that can be formed using rectangles with the same aspect ratio.
            
        for c in count.values():
            res += (c*(c-1)) // 2
            
        return res    
        
        
#solution = Solution()
#result = solution.interchangeableRectangles(rectangles)
#print(result)#        