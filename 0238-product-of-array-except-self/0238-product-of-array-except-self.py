class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ## create an array of len that of input array(nums) and initialize every element as 1
        res = [1] * (len(nums))
        
        ## prefix case 
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix*nums[i]
            
        ## postfix
        postfix = 1
        for i in  range(len(nums)-1 , -1, -1):
            res[i] = res[i]*postfix
            postfix = postfix*nums[i]
            
        return res    
        
        
# Example usage
#nums = [1, 2, 3, 4]
#solution = Solution()
#result = solution.productExceptSelf(nums)
#print(result)  # Output: [24, 12, 8, 6]#        