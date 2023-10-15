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
    
    
# Create an instance of the Solution class
#sol = Solution()

# Example test cases
#nums = [4, 5, 6, 7, 0, 1, 2]
#target1 = 0
#target2 = 3

# Call the search method to search for the targets
#result1 = sol.search(nums, target1)
#result2 = sol.search(nums, target2)

# Print the results
#print(f"Result for target1 ({target1}): {result1}")
#print(f"Result for target2 ({target2}): {result2}")    
        