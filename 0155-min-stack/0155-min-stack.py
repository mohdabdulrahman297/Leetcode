## time: o(1)
## space: o(n)

class MinStack:

    def __init__(self):
        
        ##create two stack one for regular and another for minvalue
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        ## append values into stack
        self.stack.append(val)
        
        ## check min values from the top of the stack and the input value
        
        ## non empty then proceed
        if(self.minStack):
            val = min(val, self.minStack[-1])
            
        else:
            val = min(val, val)
            
        self.minStack.append(val)
        

    def pop(self) -> None:
        
        self.stack.pop()
        self.minStack.pop()
        
        

    def top(self) -> int:
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()