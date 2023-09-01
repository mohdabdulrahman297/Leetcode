## time:o(n)
## space: o(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        ##create two pointers left and right
        res = 0
        
        l,r = 0 , len(height)-1
        
        while(l<r):
            ##calculate area 
            
            area = (r-l) * min(height[l], height[r])
            res = max(res , area)
            
            if(height[l] < height[r]):
                l+=1
                
            elif(height[l] > height[r]):
                r-=1
                
            else:
                ##this case exists for both pointer values to be equal no matter increase l or decrease r
                l+=1
                
        return res
    
    
# Create an instance of the Solution class
#solution = Solution()

# Define an input list of heights
#heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Call the maxArea function with the input list
#result = solution.maxArea(heights)

# Print the result
#print("Maximum area:", result)#    
        