## space : o(n)
## time : o(2^n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ## only add open parenthesis if opencount < n
        ## only add close parenthesis if closecount < opencount
        ## valid if open == closed == n
        
        ## initialize an empty stack
        
        stack = []
        
        res = []
        
        ## recursive approach
        def backtrack(openCount, closeCount):
            
            ##check if both open and close counts are equal
            
            if(openCount == closeCount == n):
                
                ## from that stack convert the parenthesis into string and add into result array
                
                res.append("".join(stack))
                return
            
            if(openCount < n):
                
                
                ## add open parenthesis to the stack
                stack.append("(")
                ##recursive call
                backtrack(openCount + 1, closeCount)
                stack.pop()
                
            if(closeCount < openCount):
                ## add close parentthesis to the staxk
                stack.append(")")
                backtrack(openCount, closeCount + 1)
                stack.pop()
                
        ## initialize the backtrack function with open and closose count as 0, 0
        backtrack(0, 0)
        return res
                
        