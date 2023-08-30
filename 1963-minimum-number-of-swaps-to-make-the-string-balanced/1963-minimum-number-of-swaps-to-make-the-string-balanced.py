## time:O(n)
## space: o(1)
class Solution:
    def minSwaps(self, s: str) -> int:
        
        extraClose = 0
        maxClose = 0
        
        for c in s:
            
            if c == "[":
                
                extraClose -= 1
                
            else:
                
                extraClose += 1
                
            maxClose = max(extraClose , maxClose)
            
        return (maxClose + 1)//2    
        
        
# Example usage
#if __name__ == "__main__":
    #solution = Solution()
    #input_string = "[]][[]"
    #result = solution.minSwaps(input_string)
    #print("Result:", result)#        