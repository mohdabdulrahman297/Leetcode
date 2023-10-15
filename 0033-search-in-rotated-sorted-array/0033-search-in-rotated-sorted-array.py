## space: o(1)
## time: o(logn)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ## initialize the pointers
        l, r = 0, len(nums) - 1
        
        ## iterate
        while(l <= r):
            ## calculate the mid
            m = (l+r)//2
            if(target == nums[m]):
                return m
            
            ## if we are in the left portion(sorted)
            if(nums[l] <= nums[m]):
                if(target > nums[m] or target < nums[l]):
                    ## search in right
                    l = m+1
                else:
                    r = m-1
                    
            ## if we are in the right portion(Sorted) 
            else:
                if(target < nums[m] or target > nums[r]):
                    r = m-1
                else:
                    l = m+1
                    
        return -1           
        