class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ## create an output
        
        output = []
        
        ## initialize a deuque(elements are in monotonically decreasing order)
        
        q = collections.deque()
        
        ## pointers left and right
        
        l = r = 0
        
        ## iterate in the bounds
        
        while(r < len(nums)):
            
            ##pop smaller values from q
            
            ## check if the queue if non empty and left most value is smallest to the right most value of windoe
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            ## after poping add the right most element of the window i.e the max of the window
            q.append(r)
            
            ##start removing left val from window
            ## check if the left most pointer is greter than that the next left element
            if(l > q[0]):
                q.popleft()
                
            ## check if in range add the element to the output
            
            if(r+1) >= k:
                output.append(nums[q[0]])
                ## shift the pointers
                l += 1
                
            r += 1   
            
        return output     
        