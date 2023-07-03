##time : o(n)
## space : o(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        ## total sum of the array
        total = sum(nums)
        
        leftsum = 0
        
        for i in range(len(nums)):
            rightsum = total - nums[i] - leftsum
            if(leftsum == rightsum):
                return i
            leftsum += nums[i]
        return -1    
##solution = Solution()

# Example 1
##nums = [1, 7, 3, 6, 5, 6]
##output = solution.pivotIndex(nums)
##print(output)  # Output: 3

##        