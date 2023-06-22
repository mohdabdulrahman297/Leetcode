##time:o(n)
##space:o(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for i in range(2):
            for j in nums:
                ans.append(j)
        return ans
    
    
# Create an instance of the Solution class
#solution = Solution()

# Provide a list of integers as input
#nums = [1, 2, 3, 4, 5]

# Call the getConcatenation method and store the result
#result = solution.getConcatenation(nums)

# Print the concatenated list
#print("Concatenated list:", result)
    