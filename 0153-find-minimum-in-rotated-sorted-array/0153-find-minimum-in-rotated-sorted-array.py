## space: o(1)
## time: o(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        ##initialize the pointers and result be any value
        
        l, r = 0, len(nums) - 1
        res = nums[0]
        
        
        ##iterate
        while(l <= r):
            ## check if the left most value is lesser than the right most because as per the rotation it should be
            if(nums[l] < nums[r]):
                ## if it does then update the minimun
                res = min(res, nums[l])
                break
                
            ## binary search
            m = (l+r)//2
            res = min(res, nums[m])
            if(nums[m] >= nums[l]):
                ## search in the right part
                l = m+1
            else:
                # search in the left part
                r = m-1
        return res   
    
    
# Define the input data
#nums = [4, 5, 6, 7, 0, 1, 2]

# Create an instance of the Solution class
#solution = Solution()

# Call the findMin function
#result = solution.findMin(nums)

# Print the result
#print("Minimum element in the rotated and sorted array:", result)
    
                
                