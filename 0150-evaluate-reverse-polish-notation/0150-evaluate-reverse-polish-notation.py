## space: o(n)
## time: o(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ##create an empty stack
        stack = []
        
        ## for different arthmetic operators apply the logic
        
        for c in tokens:
            if c == "+":
                ## pop those two values before the operator , apply the operation between them and add the result to the stack
                
                stack.append(stack.pop() +  stack.pop())
                
            elif c == "-":
                ## b-a gives positive values whereas a-b gives negative
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
                
            elif c == "*":
                
                stack.append(stack.pop() * stack.pop())
                
            elif c ==  "/":
                a,b = stack.pop(), stack.pop()
                ##int() rounds off the number
                stack.append(int(b/a))
                
            else:
                ## first convert string into int and then append 
                stack.append(int(c))
        
        ## the element that is left in the stack
        return stack[0]         
        
        
        
# Create an instance of the Solution class
##solution = Solution()

# Test case (RPN expression as tokens)
##tokens = ["3", "4", "+", "2", "*", "7", "/"]  # Equivalent to (3 + ##4) * 2 / 7

# Evaluate the RPN expression
##result = solution.evalRPN(tokens)

# Print the result
##print("Result:", result)  # Should print the result of the ##expression
##        