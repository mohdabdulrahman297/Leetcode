## space: o(n)
## time: o(n)

class Solution:
    def isValid(self, s: str) -> bool:
        
        ## create an empty stack
        stack = []
        ## map the closing brackets to open brackets using hashmaps
        
        closeToOpen = { ")" : "(" , "]" : "[" , "}" : "{"}
        
        ##iterate through the input string and check if the key(closing bracket in the stack) -1 is the last element of stack
        
        for c in s:
            if c in closeToOpen:
                
                if stack and stack[-1]  == closeToOpen[c]:
                    ## start popping
                    stack.pop()
                    
                else:
                    ## means there is no matching 
                    return False
                
            else:
                ## this else case inidcates the brakcet is open and hence we add it to the stack stack follows LIFO order
                stack.append(c)
                
        if not stack:
            return True
        else:
            return False
            
  # Create an instance of the Solution class
##solution = Solution()

# Test cases
##input_str1 = "()"
##input_str2 = "({[()]})"

# Check if the input strings have valid brackets
##print(solution.isValid(input_str1))  # Should print True
##print(solution.isValid(input_str2))  # Should print True
##      