## time: o(nlogn)
## space : o(n)

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ##create a pair of both the position and speed arrays
        
        pair = [(p, s) for p, s in zip(position, speed)]
        
        ##create an empty stack
        stack = []
        
        ## iterate the pair in reverse order after sorting it
        for p, s in sorted(pair)[::-1]:
            
            ## calculate the distance for each car and append it to the stack
            stack.append((target - p) / s)
            
            ## check if there are two elements in the stack because lesser distance will collide with another so there must be two elements in the stack.
            
            ## check if the 2nd distance is greater than the first distance 
            
            if(len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()
                
        return len(stack)       