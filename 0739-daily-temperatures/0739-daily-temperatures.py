## space: o(n)
## time: o(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ##initialize a result array of length same as input array with default values as '0'
        
        res = [0] * len(temperatures)
        
        
        ##initializw a stack with pair values
        
        stack = []
        ## pair : [temp, index]
        
        ## itetate and keep track of both the value and index in the input array
        
        for i,t in enumerate(temperatures):
            
            ## check if the stack is not empty and temperature value is greater than stack top value
            
            while stack and t > stack[-1][0]:
                
                ## pop those value and index from the stack
                stackTop, stackIndex = stack.pop()
                
                ## append the difference into result
                
                res[stackIndex] = i - stackIndex
            stack.append((t, i))
                
        return res         
                
        