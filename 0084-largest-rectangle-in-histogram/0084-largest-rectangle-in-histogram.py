## time: o(n)
## space : o(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ## initialize maxarea as '0'
        maxArea = 0
        
        ## a stack with pair : (index:height)
        stack = []
        
        ## interate for both index and height in input array
        
        for i, h in enumerate(heights):
            
            ## let the start be i(initially)
            
            start = i
            
            ## when stack not empty and stack top value is greater than height
            
            while stack and stack[-1][1] > h:
                ## pop and store in index, height
                index, height = stack.pop()
                ## area is height * width where width is i-index
                maxArea = max(maxArea, height * (i-index))
                ##update start
                start = index
                
            stack.append((start, h))
            
        ## now check for the values left in the stack
        for i, h in stack:
            
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea   
        
                
        