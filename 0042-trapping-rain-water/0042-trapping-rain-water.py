class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            
            rightMax = max(rightMax, height[r])
            
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                
        return res
    
    
 # Create an instance of the Solution class
#solution = Solution()

# Define an input list of heights
#heights = [0,1,0,2,1,0,1,3,2,1,2,1]

# Call the trap function with the input list
#result = solution.trap(heights)

# Print the result
#print("Trapped water units:", result)#   
